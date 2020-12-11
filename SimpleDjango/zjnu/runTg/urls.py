from django.urls import path
from . import views

urlpatterns = {
	path('', views.show, name='show'),
	path('show/', views.show, name='show'),
	path('insert/', views.insert, name='insert'),
    path('join/', views.join, name='join'),
}
