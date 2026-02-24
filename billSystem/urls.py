from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('loginn/', views.loginn, name='loginn'),
    path('logout/', views.logout, name='logout'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('training-bills/', views.training_bills, name='training_bills'),
    path('view-users/', views.view_users, name='view_users'),
    path('reminder/', views.reminder, name='reminder'),
]
