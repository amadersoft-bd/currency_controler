from django.urls import path
from . import views


urlpatterns = [
	path('', views.admin_dashboard, name ='admin_dashboard'),
	path('test/', views.test, name ='test'),
]