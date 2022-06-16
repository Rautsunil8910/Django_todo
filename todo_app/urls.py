from django.urls import path
from .import views

urlpatterns = [
    path('',views.home , name='home'),
    path('delete/<int:i>',views.delete ,name='delete'),
    path('update/<int:i>',views.update ,name='update'),
    path('search/',views.search ,name='search'),
    
]