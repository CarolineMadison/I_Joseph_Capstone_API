import sqlite3
from django.shortcuts import render, redirect, reverse
from ijosephapp.models import Job
from ..connection import Connection
from ijosephapp.models import JobCategory, UserJob
from ijosephapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def job_list(request):
    if request.method == 'GET':
        
        all_jobs = Job.objects.all()
        user_jobs = UserJob.objects.all()
        notcheckedout_jobs = []
        for job in all_jobs:
            jobcheckedoutcount = user_jobs.filter(job_id=job.id).count()
            print('debugme: job.id ' + str(job.id) + " " + job.title + " " + str(jobcheckedoutcount) )
            if jobcheckedoutcount == 0:
                notcheckedout_jobs.append(job)
        template = 'jobs/list.html'

        context = {
            'notcheckedout_jobs': notcheckedout_jobs
        }
       
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        if form_data["actionType"] == "Update":
            #update code here
            isCompleted = form_data.get("isCompleted", False)
            job_id = form_data["job_to_edit_id"]
            updatedtitle = form_data["title"]
            print("Debug in job update, the job_to_edit_id: " + str(job_id) + " title, " + updatedtitle)

            Job.objects.filter(pk=job_id).update(title=updatedtitle)

            # updated_job = Job(
            #     title = form_data['title']
            #     # category_id = form_data['category'],
            #     # location = form_data['location'],
            #     # description = form_data['description'],
            #     # isCompleted = isCompleted,
            #     # user_id = request.user.id
            # )
            # updated_job.update()

        elif form_data["actionType"] == "NewJob":

            #this is a new record so add the object here
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