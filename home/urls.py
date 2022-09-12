from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('generate/<int:pk>', views.generate.as_view(), name='generate'),
]
