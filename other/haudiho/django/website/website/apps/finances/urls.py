from django.urls import path

from . import views

app_name = "finances"
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.get_money, name='all_money'),
   ]

