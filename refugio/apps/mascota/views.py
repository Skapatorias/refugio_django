from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls    import reverse_lazy

from apps.mascota.forms     import MascotaForm
from apps.mascota.models    import Mascota
# Create your views here.


def index(request):
    return render(request, 'mascota/index.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('listar')

    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}

    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect ('listar')
    return render(request, 'mascota/mascota_form.html', {'form':form})


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'


class MascotaCrear(CreateView):
    model = Mascota
    fields = ['nombre', 'sexo', 'edad_aproximada', 'fecha_rescate', 'persona', 'vacuna']
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('listar')

class MascotaUpdate(UpdateView):
    model = Mascota
    fields = ['nombre', 'sexo', 'edad_aproximada', 'fecha_rescate', 'persona', 'vacuna']
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('listar')