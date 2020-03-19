import sqlite3
from django.shortcuts import render, redirect, reverse
from ijosephapp.models import Job
from ijosephapp.models import UserJob
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def userjob_list(request):
    if request.method == 'GET':
        
        # user_id = request.user.id
        # all_userjobs = UserJob.objects.filter all()
        all_userjobs = UserJob.objects.all()

        template = 'userjob/list.html'

        context = {
            'all_userjobs': all_userjobs
        }
       
        return render(request, template, context)

        # filter by user id in the html
    
    elif request.method == 'POST':
        form_data = request.POST
    #    this will come from the hidden input fields on detail.html
        new_userjob = UserJob(
            job_id = form_data["job_id"],
            user_id = request.user.id
        )

        new_userjob.save()

        return redirect(reverse('ijosephapp:userjob'))