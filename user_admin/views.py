from django.shortcuts import render

# Create your views here.
def user_admin(request):

	return render(request, 'admin/user_admin/user_admin.html')