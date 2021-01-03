from django.urls import path
from . import views


urlpatterns = [
	path('agent/', views.agent, name = 'agent'),

]