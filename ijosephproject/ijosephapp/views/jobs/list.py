import sqlite3
from django.shortcuts import render, redirect, reverse
from ijosephapp.models import Job
from ..connection import Connection
from ijosephapp.models import JobCategory, UserJob
from django.contrib.auth.decorators import login_required

@login_required
def job_list(request):
    if request.method == 'GET':
        
        user = request.user.id

        all_jobs = Job.objects.all()
    
        # gets all jobs user has submitted
        yoursubmittedjobs = Job.objects.filter(user=user).first()

        print('THESE ARE THE SUBMITTED JOBS: ' + str(yoursubmittedjobs))

        user_jobs = UserJob.objects.all()

        notcheckedout_jobs = []
        for job in all_jobs:
            # checking in userjob relationship to see if job is checked out
            jobcheckedoutcount = user_jobs.filter(job_id=job.id).count()
            print('debugme: job.id ' + str(job.id) + " " + job.title + " " + str(jobcheckedoutcount) + " " + str(job.user_id))
            # if the job is not checked out and the current user didn't create it
            if jobcheckedoutcount == 0 and job.user_id != user:
                # put that job into the notcheckedout_jobs
                notcheckedout_jobs.append(job)

        notcheckedout_jobs_count = len(notcheckedout_jobs)

        template = 'jobs/list.html'

        context = {
            'notcheckedout_jobs': notcheckedout_jobs,
            'notcheckedout_jobs_count': notcheckedout_jobs_count,
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

            Job.objects.filter(pk=job_id).update(
                title = form_data["title"],
                location = form_data["location"],
                description = form_data["description"]
    
                )

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

        return redirect(reverse('ijosephapp:yourjob'))