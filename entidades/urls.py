from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import agenda_view, CustomLoginView, registro_view

urlpatterns = [
    path('', agenda_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', registro_view, name='registro'),
    ] 
 
