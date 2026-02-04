from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('index',views.index),
    path('login',views.login),
    path('loginn',views.loginn),
    path('logout',views.logout),
    path('about_us',views.about_us),
    path('contact',views.contact),
    path('services',views.services),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
