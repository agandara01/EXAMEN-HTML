from django.urls import path
from . import views


# Cuando se conecte por primera vez a mi pagina se conectara a index
urlpatterns = [
    path('',views.index,name="index"),
    path('registro/', views.registro, name="registro"),
    path('registro/crear',views.crear, name="crear"),
]
