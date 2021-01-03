from django.shortcuts import render

# Create your views here.
def agent(request):

	return render(request, 'users/agent/agent.html')