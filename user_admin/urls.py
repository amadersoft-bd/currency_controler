from django.urls import path
from . import views


urlpatterns = [
	path('', views.user_admin, name ='user_admin'),

]