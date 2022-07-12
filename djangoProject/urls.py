
from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create)
]
