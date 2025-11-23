from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CredentialsModel
from visitors.models import Visitor
from datetime import timedelta
from django.utils import timezone
import random

def Asign_credential(request):
    context = {}
    expiration_days = {
        'TEMP': 2,
        'PROV': 5,
        'EMP': 14,
    }
    context['expiration_days'] = expiration_days

    visitor_id = request.GET.get('visitor_id') or request.POST.get('visitor_id')
    visitor = None
    if visitor_id:
        visitor = get_object_or_404(Visitor, pk=visitor_id)
        context['current_days'] = expiration_days.get(visitor.visitor_type)
        context['visitor_type_label'] = visitor.get_visitor_type_display()

    def generate_unique_code():
        code = None
        for _ in range(10):
            candidate = str(random.randint(0, 999999)).zfill(6)
            if not CredentialsModel.objects.filter(credential_code=candidate).exists():
                code = candidate
                break
        return code

    if request.method == 'POST':
        if not visitor:
            messages.error(request, 'Visitante no especificado.')
            return redirect('dashboard')

        credential_code = (request.POST.get('credential_code') or '').strip()
        if not credential_code:
            messages.error(request, 'No se pudo obtener el codigo de credencial.')
            context['preview_code'] = generate_unique_code()
            context['visitor'] = visitor
            return render(request, 'credentials/create_credential.html', context)

        if CredentialsModel.objects.filter(credential_code=credential_code).exists():
            messages.error(request, 'El codigo ya fue asignado, genera uno nuevo.')
            context['preview_code'] = generate_unique_code()
            context['visitor'] = visitor
            return render(request, 'credentials/create_credential.html', context)

        cred = CredentialsModel(visitor=visitor)
        cred.credential_code = credential_code
        days = expiration_days.get(visitor.visitor_type, 2)
        cred.expiration_date = timezone.now() + timedelta(days=days)
        cred.save()
        messages.success(request, 'Credencial digital generada correctamente!')
        return redirect('dashboard')

    preview = generate_unique_code()
    context['form'] = None
    context['visitor'] = visitor
    context['preview_code'] = preview
    return render(request, 'credentials/create_credential.html', context)

   
