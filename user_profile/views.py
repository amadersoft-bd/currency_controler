from agent.models import Agent
from django.contrib.auth.backends import UserModel
from django.core import exceptions
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Package, Profile
from django.contrib import auth
from django.contrib.auth.models import User
from .utils import create_new_ref_number
from .forms import InfoProfileForm,ProfileForm

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/profile/login/')
def profile(request):

	# profile_data = Profile.objects.get(user=request.user)
	# context = {
	# 	'profile_data': profile_data,
	# }

	return render(request, 'users/user_profile/profile.html')

@login_required(login_url='/profile/login/')
def update_profile(request):
	#selected_package = None
	package_id = Package.objects.all()
	
	if request.method == "POST":
		
		try:
			profile = Profile.objects.get(id=request.user.id)
			
		
			#user = User.objects.get(username = request.POST['username'],email = request.POST['email'])
			full_name = request.POST.get('full_name')
			address = request.POST.get('address')
			country = request.POST.get('country')
			#tnx_no = create_new_ref_number() #request.POST.get('tnx_no')
			 #request.POST.get('agent_id')
				#package_id =Package.objects.get(id)
			photo = request.FILES.get('photo')	
			#pk_id = request.POST.get('package_name')
			#package_id =Package.objects.get(id=pk_id)
			#print(package_id)

			mobile_no = request.POST.get('mobile_no')
			birth_date = request.POST.get('birth_date')
			#profile = Profile(full_name=full_name,photo=photo,address=address,country=country,mobile_no=mobile_no,birth_date=birth_date, )
			profile.full_name=full_name
			profile.address = address
				
			profile.save()
			return render(request, 'users/user_profile/profile.html')
		except User.DoesNotExist:		
			
				#auth.login(request,user)
				#return render(request, 'users/user_profile/signup.html')
			return render(request, 'users/user_profile/update_profile.html')

	else:
		context ={
			     #'selected_package':selected_package,
			'package_id': package_id,
					}
		return render(request, 'users/user_profile/update_profile.html',context)
	

def registration(request):
	#selected_package = None
	package_id = Package.objects.all()
	
	if request.method == "POST":
		#profile_form = UserProfileForm(request.POST)
		if request.POST['password'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'users/account/registration.html',{'error': "username has already taken"})
			except User.DoesNotExist:
				user = User.objects.create_user(username = request.POST['username'],email = request.POST['email'],password=request.POST['password'])
				full_name = request.POST.get('full_name')
				address = request.POST.get('address')
				country = request.POST.get('country')
				tnx_no = create_new_ref_number() #request.POST.get('tnx_no')
				agent_id =Agent.objects.get(id=2) #request.POST.get('agent_id')
				#package_id =Package.objects.get(id)
				sponsor_id = request.POST.get('sponsor_id')
				pk_id = request.POST.get('package_name')
				package_id =Package.objects.get(id=pk_id)
				print(package_id)

				mobile_no = request.POST.get('mobile_no')
				birth_date = request.POST.get('birth_date')
				profile = Profile(full_name=full_name,agent_id=agent_id,sponsor_id=sponsor_id,package_id =package_id,tnx_no=tnx_no,address=address,country=country,mobile_no=mobile_no,birth_date=birth_date, user=user)
				
				profile.save()
				
			
				#auth.login(request,user)
				#return render(request, 'users/user_profile/signup.html')
				return render(request, 'users/account/registration.html')

		else:
			return render(request, 'users/account/registration.html')
	
	
	else:
		#return render(request, 'users/user_profile/signup.html')
		
		context ={
			     #'selected_package':selected_package,
				 'package_id': package_id,
					}
		return render(request, 'users/account/registration.html',context)



#login code
def login(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
		#if not request.user.is_authenticated:
			
			auth.login(request, user)
			
			print("submitted")
			return render(request, 'users/user_profile/profile.html')
		else:
			return render(request,'users/account/login.html')

	else:
		return render(request,'users/account/login.html')

@login_required(login_url='/profile/login/')
def logout(request):
	auth.logout(request)
	return render(request, 'users/index.html')