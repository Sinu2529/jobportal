from django.contrib import admin
from users.models import jobs

class JobAdmin(admin.ModelAdmin):
    list_display=('title','desp','job_type','stipend')

admin.site.register(jobs,JobAdmin)
# Register your models here.
