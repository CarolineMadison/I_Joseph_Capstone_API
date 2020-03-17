import sqlite3
from django.shortcuts import render, redirect, reverse
from ijosephapp.models import Job
from ..connection import Connection
from ijosephapp.models import JobCategory
from ijosephapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def job_list(request):
    if request.method == 'GET':
        
        all_jobs = Job.objects.all()

        template = 'jobs/list.html'

        context = {
            'all_jobs': all_jobs
        }
       
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        isCompleted = form_data.get("isCompleted", False)
       
        new_job = Job(
            title = form_data['title'],
            category_id = form_data['category'],
            location = form_data['location'],
            description = form_data['description'],
            isCompleted = isCompleted,
            user_id = request.user.id
        )

        new_job.save()

        return redirect(reverse('ijosephapp:jobs'))