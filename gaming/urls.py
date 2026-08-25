from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pro', views.pro, name='pro'),
    path('newbie', views.newbie, name='newbie'),
    path('thanks', views.thanks, name='thanks'),
]