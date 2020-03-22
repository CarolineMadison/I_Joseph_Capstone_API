import sqlite3
from django.shortcuts import render, redirect, reverse
from ijosephapp.models import Job
from ijosephapp.models import UserJob
from ..connection import Connection
from django.contrib.auth.decorators import login_required

# this renders the page
@login_required
def yourjobs_list(request):
    if request.method == 'GET':
        
        # gets the id of the logged in user
        user = request.user.id

        # Get all jobs user has checked out 
        yourjobs = UserJob.objects.filter(user_id=user)

        # Get all jobs user has submitted
        yoursubmittedjobs = Job.objects.filter(user=user)
        
        #Init new array to hold jobs the user has checked out
        checkedout_jobs = []

        #For each checked out job relationship
        for yourjob in yourjobs:
            #Grab the job id
            tempId = yourjob.job_id
            #Filter the jobs for those that match the job id
            #The .first() is required to return the actual object not a queryset 
            tempObject = Job.objects.filter(id=tempId).first()
            print('debug me: ' + tempObject.title)
        
            # takes all of the relationships in the userjob table and puts them into a new array of job objects where the user_id is the logged in user
            checkedout_jobs.append(tempObject)
        
        checkedout_job_count = 0
        for checkedout_job in checkedout_jobs:
            if checkedout_job.isCompleted == False:
                checkedout_job_count = checkedout_job_count + 1

            

        print("Your Job Count: " + str(checkedout_job_count))

        template = 'userjob/yourjobs_list.html'
        
        # sends the arrays of objects to the template
        context = {
            'yourjobs': yourjobs,
            'yoursubmittedjobs': yoursubmittedjobs,
            'checkedout_jobs': checkedout_jobs,
            'checkedout_job_count': checkedout_job_count
        }
       
        return render(request, template, context)

    # handles post events driven by the buttons on the page
    elif request.method == 'POST':
        form_data = request.POST

        print(form_data)

        # handles creating a new user job relationship when a user selects a job
        if form_data["actionType"] == "SelectOpportunity":
   
            new_userjob = UserJob(
                job_id = form_data["job_id"],
                user_id = request.user.id
            )
            print("this is select opportunity")

            new_userjob.save()

        # For changing the boolean on the Job table to isComplete=True 
        elif form_data["actionType"] == "MarkComplete":
            # grabs the value for the keyname job_id from the form data
            job_id = form_data["job_id"]
            # Filters the Job table where the Job id === the job_id from the form data
            Job.objects.filter(id=job_id).update(isCompleted=True) 

        # For deleting a single userjob relationship
        elif form_data["actionType"] == "Deselect":
            # grabs the value for the keyname other_job_id from the form data
            other_job_id = form_data["other_job_id"]
            tempCount = UserJob.objects.filter(job=other_job_id).count()

            # this filters the userjob table, finds all records in the database where job_id === job.id
            UserJob.objects.filter(job=other_job_id).delete()

            print("this is the deselect for userjob relationship " + str(other_job_id) + " count: " + str(tempCount))

        # For deleting a job from the job table
        elif form_data["actionType"] == "Delete":
            # grabs the value for the keyname other_job_id from the form data
            other_job_id = form_data["other_job_id"]
            Job.objects.filter(id=other_job_id).delete()

            print("this is the delete button for job id " + other_job_id)

    return redirect(reverse('ijosephapp:yourjob'))

















