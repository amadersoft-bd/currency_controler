from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'users/index.html')
    # return render(request, 'landing/index.html') 


def login(request):
    
    return render(request, 'users/account/login.html')


def registration(request):
    return render(request, 'users/account/registration.html')

def update_profile(request):
    return render(request, 'users/user_profile/update_profile.html')

def profile(request):
    return render(request, 'users/user_profile/profile.html')

def downline_link(request):
    return render(request, 'users/user_profile/downline_network.html')

def dash_board(request):
    return render(request, 'users/user_profile/dash_board.html')


def sponsor_reports(request):
    return render(request,'users/reports/sponsor_reports.html')

def exchange_reports(request):
    return render(request,'users/reports/exchange_reports.html')

def transfer_reports(request):
    return render(request,'users/reports/transfer_report.html')

def balance_add(request):
    return render(request,'users/balance/balance_add.html')


def balance_withdrow(request):
    return render(request,'users/balance/balance_withdrow.html')


def balance_transfer(request):
    return render(request,'users/balance/balance_transfar.html')
