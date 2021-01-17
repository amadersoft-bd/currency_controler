from user_admin.forms import NotificationForm
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Notification
from django.db.models import Count  
from django.utils import timezone  
# Create your views here.
def admin_dashboard(request):
	notific = Notification.objects.order_by('-duration')[:4]
	#notification_count = Notification.objects.annotate(total_notification = Count('notific'))
	notification_count = Notification.objects.filter(created__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).count()
	print(notification_count)
	context ={
		'notific': notific,
		'notification_count':notification_count,
	}
	return render(request, 'admin/admin_index.html',context)


def test(request):
    if request.method=='POST':
        form=NotificationForm(request.POST)
        if form.is_valid():
            #cementry is a variable
			
            ce =form.save(commit=False)
			
            ce.title=request.POST.get('title')
            ce.body=request.POST.get('body')
            ce.status=request.POST.get('status')
            ce.duration = request.POST.get('duration')
            ce.save() 
       
            return render(request, 'admin/user_admin/test.html')  
        else:
            # If the request was not a POST, display the form to enter details.
            #messages.error(request, 'You are messages can not submitted.')
       
            return render(request, 'admin/user_admin/test.html')  

    else:
        form=NotificationForm
    return render(request,'admin/user_admin/test.html',{'form':form})