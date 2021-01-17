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
    path('balance_withdrow/',views.balance_withdrow, name='balance_withdrow'),
    path('balance_transfer/',views.balance_transfer, name='balance_transfer'),
    path('holdline_list7/',views.holdline_list7, name='holdline_list7'),
    path('pakage_line_member7/',views.pakage_line_member7, name='pakage_line_member7'),
    path('agent_list7/',views.agent_list7, name='agent_list7'),
    path('new_member7/',views.new_member7, name='new_member7'),
    path('add_member7/',views.add_member7, name='add_member7'),
    path('notification_list7/',views.notification_list7, name='notification_list7'),
    ]
