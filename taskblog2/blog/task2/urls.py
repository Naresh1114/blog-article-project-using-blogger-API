from django.urls import path
from . import views

urlpatterns = [
    path('',views.content,name='home'),
    path('final/<str:id>/',views.final,name='final'),
]




