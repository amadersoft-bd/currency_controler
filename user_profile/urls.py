from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.profile, name='user_profile'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login, name='login'),
	
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/user_profile/password_reset.html'), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/user_profile/password_reset_done.html'), name='password_reset_done'),
	path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/user_profile/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/user_profile/password_reset_complete.html'), name='password_reset_complete'),
]