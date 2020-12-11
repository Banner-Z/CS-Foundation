from django.urls import path
from . import views

urlpatterns = {
	path('', views.index, name='index'),
    path('agency/', views.agency, name='agency'),
    path('deal/', views.deal, name='deal'),
    path('details/', views.details, name='details'),
}
