from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import vehiculos
from .forms import VehicleForm

# Create your views here.

def create_view (request):
    context = {}
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context = {'form': form}
    return render(request, "create_view.html", context)

def list_view (request):
    context = {}
    context['database'] = vehiculos.objects.all()
    return render(request, "list_view.html", context)

def update_view (request, id):
    context = {}

    obj = get_object_or_404(vehiculos, id=id)

    form = VehicleForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context["form"] = form

    return render(request, "update_view.html", context)

def delete_view (request, id):
    context = {}
    obj = get_object_or_404(vehiculos, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "delete_view.html", context)
