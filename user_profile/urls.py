from django.urls import path
from . import views


urlpatterns = [
	path('', views.profile, name='user_profile'),
	path('signup/', views.signup, name='signup'),

]