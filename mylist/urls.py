from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.schedule_create, name='schedule_create'),
    path('delete/<int:schedule_id>', views.schedule_delete, name='schedule_delete'),
]