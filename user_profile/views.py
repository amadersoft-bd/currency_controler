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
@login_required
def profile(request):

	profile_data = Profile.objects.get(user=request.user)
	context = {
		'profile_data': profile_data,
	}
	return render(request, 'users/user_profile/profile_test.html',context)
def edit_profile(request):
	# profile_data = Profile.objects.get(user__id=request.user.id)
	# package_id = Package.objects.all()
	
	# if request.method == "POST":
	# 	#profile_form = UserProfileForm(request.POST)
	# 	if request.POST['password'] == request.POST['password2']:
	# 		try:
	# 			user = User.objects.get(username=request.POST['username'])
	# 			return render(request, 'users/user_profile/signup.html',{'error': "username has already taken"})
	# 		except User.DoesNotExist:
	# 			user = User.objects.create_user(username = request.POST['username'],email = request.POST['email'],password=request.POST['password'])
	# 			full_name = request.POST.get('full_name')
	# 			address = request.POST.get('address')
	# 			country = request.POST.get('country')
	# 			tnx_no = create_new_ref_number() #request.POST.get('tnx_no')
	# 			agent_id =Agent.objects.get(id=2) #request.POST.get('agent_id')
	# 			#package_id =Package.objects.get(id)
	# 			photo = request.POST.get('photo')
	# 			birth_date = request.POST.get('birth_date')
	# 			pk_id = request.POST.get('package_name')
	# 			package_id =Package.objects.get(id=pk_id)
	# 			print(package_id)

	# 			mobile_no = request.POST.get('mobile_no')
	# 			birth_date = request.POST.get('birth_date')
	# 			profile = Profile(full_name=full_name,photo=photo,agent_id=agent_id,package_id =package_id,tnx_no=tnx_no,address=address,country=country,mobile_no=mobile_no,birth_date=birth_date, user=user)
				
	# 			profile.save()
				
			
	# 			#auth.login(request,user)
	# 			return render(request, 'users/user_profile/profile.html')

	# 	else:
	# 		return render(request, 'users/user_profile/profile.html')
	
	
	# else:
	# 	#return render(request, 'users/user_profile/signup.html')
		
	# 	context ={
	# 		     #'selected_package':selected_package,
	# 			 'profile_data':profile_data,
	# 			 'package_id': package_id,
	# 				}
	return render(request, 'users/user_profile/edit_profile.html')
	





def signup(request):
	#selected_package = None
	package_id = Package.objects.all()
	
	if request.method == "POST":
		#profile_form = UserProfileForm(request.POST)
		if request.POST['password'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'users/user_profile/signup.html',{'error': "username has already taken"})
			except User.DoesNotExist:
				user = User.objects.create_user(username = request.POST['username'],email = request.POST['email'],password=request.POST['password'])
				full_name = request.POST.get('full_name')
				address = request.POST.get('address')
				country = request.POST.get('country')
				tnx_no = create_new_ref_number() #request.POST.get('tnx_no')
				agent_id =Agent.objects.get(id=2) #request.POST.get('agent_id')
				#package_id =Package.objects.get(id)
				
				pk_id = request.POST.get('package_name')
				package_id =Package.objects.get(id=pk_id)
				print(package_id)

				mobile_no = request.POST.get('mobile_no')
				birth_date = request.POST.get('birth_date')
				profile = Profile(full_name=full_name,agent_id=agent_id,package_id =package_id,tnx_no=tnx_no,address=address,country=country,mobile_no=mobile_no,birth_date=birth_date, user=user)
				
				profile.save()
				
			
				#auth.login(request,user)
				return render(request, 'users/user_profile/signup.html')

		else:
			return render(request, 'users/user_profile/signup.html')
	
	
	else:
		#return render(request, 'users/user_profile/signup.html')
		
		context ={
			     #'selected_package':selected_package,
				 'package_id': package_id,
					}
		return render(request, 'users/user_profile/signup.html',context)



#login code
def login(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
		#if not request.user.is_authenticated:
			profiles_data = Profile.objects.filter(user=request.user)
			auth.login(request, user)
			
			print("submitted")
			return render(request, 'users/user_profile/profile_test.html',{'profiles_data':profiles_data,})
		else:
			return render(request,'users/user_profile/login.html')

	else:
		return render(request,'users/user_profile/login.html')
		
