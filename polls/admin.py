from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.register(Subscriber)
admin.site.unregister(Group)		

class PostAdmin(admin.ModelAdmin):
	list_display = ['id','name','description','author','date']
	exclude = ['id']	
	list_filter = ('author','date')
		
admin.site.register(Post, PostAdmin)


