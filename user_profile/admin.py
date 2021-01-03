from django.contrib import admin

# Register your models here.
from .models import Package,UsePositionStatus,Profile
# Register your models here.
admin.site.register(Package)
admin.site.register(UsePositionStatus)
admin.site.register(Profile)