from agent.models import Agent
from django.contrib.auth.backends import UserModel
from django.core import exceptions
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Package, Profile
from django.contrib import auth
from django.contrib.auth.models import User
from .utils import create_new_ref_number
from .forms import InfoProfileForm,ProfileForm
# Create your views here.
def profile(request):

	return render(request, 'users/user_profile/profile.html')

# def signup(request):
# 	register = False
# 	if request.method == "POST":
		
# 		profile_form = ProfileForm(data=request.POST)
# 		info_form = InfoProfileForm(data=request.POST)

# 		if profile_form.is_valid() and info_form.is_valid():
# 			user = profile_form.save()
# 			user.save()
# 			profile = info_form.save(commit=False)
# 			profile.user=user
# 			profile.save()
# 			print("submited..........")
# 			register=True
# 			#username = form.cleaned_data.get('username')
# 			#password= form.cleaned_data.get('password')
# 			#user = auth.authenticate(username=username,password=password)
# 			#login(request,user)

			
# 		else:
# 			return HttpResponse("something wrong")

# 	else:
# 		profile_form = ProfileForm(data=request.POST)
# 		info_form = InfoProfileForm(data=request.POST)
		 
# 	context ={
# 		'register': register,
# 		'info_form': info_form,
# 		'profile_form': profile_form,
# 	}
# 	return render(request, 'users/user_profile/signup.html',context)




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
				user = User.objects.create_user(username = request.POST['username'],password=request.POST['password'])
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