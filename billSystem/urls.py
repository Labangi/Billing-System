from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('login',views.index),
    path('loginn',views.loginn),
    path('logout',views.logout),

]