from django.urls import path
from login import views

urlpatterns = [
    path("home/", views.home_usuario, name="home-usuario"),
    path("delete/", views.deleteall, name="delete-all"),
    path("crear_usuario/", views.crear_usuario, name="crear-usuario"),
    path("login/", views.login, name="iniciar-sesion"),
    path('setup/<uidb64>/<token>/', views.confirm_url, name ='setup'),

    # falta reset
]

