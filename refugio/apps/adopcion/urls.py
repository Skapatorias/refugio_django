from django.urls import path, include
from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete


urlpatterns = [
    path('index', index),
    path('solicitud/listar', SolicitudList.as_view(), name="solicitud_listar"),
    path('solicitud/nueva', SolicitudCreate.as_view(), name="solicitud_crear"),
    path('solicitud/editar/<pk>', SolicitudUpdate.as_view(), name="solicitud_editar"),
    path('solicitud/eliminar/<pk>', SolicitudDelete.as_view(), name="solicitud_delete"),
]
