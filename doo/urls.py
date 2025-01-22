from django.urls import path 
from . import views

urlpatterns = [
    path('form/', views.form, name='forms'),
    path('seucces/', views.succ, name='seucces'),
    path('create/', views.create, name='create'),
    path('', views.tem, name='main'),
    path('trans', views.trans, name='trans'),
    path('data', views.data, name='data'),
    path('myaccount', views.account, name='MYacc'),
    path('acc/<int:pk>', views.Acc, name='acc'),
    path('tt', views.tt, name='acc'),
]


