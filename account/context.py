from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from agent.models import Agent
from user_profile.models import Profile

def user_type(request):
    if request.user.is_authenticated:
        if Agent.objects.filter(user=request.user).exists():
            print('agent')
            return {'usertype': 'agent'}
        else:
            print('user')
            return {'usertype': 'user'}
    else:
        return {'usertype': 'anonymous'}

def user_profile(request):
    if request.user.is_authenticated:
        if Agent.objects.filter(user=request.user).exists():
            
            profile = Agent.objects.get(user=request.user)
            print(profile.address)
            return {'profile': profile}

        else:
            profile = Profile.objects.filter(user=request.user)
            return {'profile': profile}
    else:
        return {'usertype': 'anonymous'}