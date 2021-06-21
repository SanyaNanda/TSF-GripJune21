from django.urls import path
from .views import home, success, mid

urlpatterns = [
    path('', home, name='home'),
    path('mid' , mid , name='mid'),
    path('success' , success , name='success')
]