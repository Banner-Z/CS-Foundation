from django.urls import path
from . import views

urlpatterns = {
	path('', views.login, name='login'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
    path('userpage/', views.userpage, name='userpage'),
}
