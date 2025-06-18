from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   
    path('menu/', views.menu_principal, name='menu'),
    path('ingresar/', views.ingresar_cv, name='ingresar_cv'),
    path('ingresar/', views.ingresar_cv, name='ingresar_cv'),
    path('listar/', views.listar_cvs, name='listar_cvs'),
    path('detalle/<int:cv_id>/', views.detalle_cv, name='detalle_cv'),

]
