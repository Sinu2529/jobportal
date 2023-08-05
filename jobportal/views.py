from django.http import HttpResponse
from django.shortcuts import render
from users.models import jobs

def home(request):
    jobsdata=jobs.objects.all()
    data={
        'jobsdata':jobsdata
    }
    return render(request,"index.html",data)