from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
class projectInline(admin.TabularInline):
	model = project
	extra = 0

class projectAdmin(admin.ModelAdmin):
	inlines = [projectInline]

admin.site.register(projectUser, projectAdmin)

admin.site.register(slide)
# admin.site.register(project)