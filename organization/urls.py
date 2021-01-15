from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login, name='login'),
    #path('registration/', views.registration, name='registration'),
    # path('update_profile/', views.update_profile, name='update_profile'),
    # path('profile/', views.profile, name='profile'),
    path('downline_link/', views.downline_link, name='downline_link'),
    path('dash_board/',views.dash_board, name='dash_board'),
    path('sponsor_reports/',views.sponsor_reports, name='sponsor_reports'),
    path('exchange_reports/',views.exchange_reports, name='exchange_reports'),
    path('transfer_reports/',views.transfer_reports, name='transfer_reports'),
    path('balance_add/',views.balance_add, name='balance_add'),
   
    ]
