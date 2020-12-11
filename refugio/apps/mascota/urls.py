from django.urls import path, include
from apps.mascota.views  import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCrear, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', MascotaCrear.as_view(), name='mascota_crear'),
    path('listar', MascotaList.as_view(), name='listar'),
    path('editar/<pk>', MascotaUpdate.as_view(), name= 'mascota_editar'),
    path('eliminar/<pk>', MascotaDelete.as_view(), name= 'mascota_eliminar'),
]