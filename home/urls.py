from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('krishna/', admin.site.urls),
    path('', views.index, name='index'),
    path('task/', views.task, name='task')
]
