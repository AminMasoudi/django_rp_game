from django.contrib import admin
from .models import UserProfile, Roles
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Roles)