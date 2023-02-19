from . import views
from django.urls import path

urlpatterns = [
    path('',views.Login,name='Login'),
    path('logout/',views.logout,name='logout')

]
