import sqlite3
from django.shortcuts import render, redirect, reverse
from ijosephapp.models import Job
from ijosephapp.models import UserJob
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def yourjobs_list(request):
    if request.method == 'GET':
        
        user = request.user.id

        # GET ALL USER JOBS FILTERED BY LOGGED IN USER
        
        yourjobs = UserJob.objects.filter(user_id=user)
        yoursubmittedjobs = Job.objects.filter(user=user)
        
        #all_jobs = Job.objects.all()
        #print('debug me: ' + str(all_jobs.count()))
        
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
            # if checkedout_jobs.count == 0:
            #     checkedofut_jobs = tempObject
            # else:
            checkedout_jobs.append(tempObject)

                
    
	
# from ijosephapp_job
# Left join ijosephapp_userjob ON ijosephapp_job.id = ijosephapp_userjob.id
# WHERE ijosephapp_userjob.user_id = 2;

        template = 'userjob/yourjobs_list.html'

        context = {
            'yourjobs': yourjobs,
            'yoursubmittedjobs': yoursubmittedjobs,
            'checkedout_jobs': checkedout_jobs
        }
       
        return render(request, template, context)

        # filter by user id in the html
    
    elif request.method == 'POST':
        form_data = request.POST
        
        print(form_data)

        if form_data["actionType"] == "SelectOpportunity":
    #    this will come from the hidden input fields on detail.html
            new_userjob = UserJob(
                job_id = form_data["job_id"],
                user_id = request.user.id
            )
            print("this is select opportunity")

            new_userjob.save()


        elif form_data["actionType"] == "MarkComplete":
            job_id = form_data["job_id"]
            Job.objects.filter(id=job_id).update(isCompleted=True)
            # print(jobtomarkcomplete.isComplete)
            # jobtomarkcomplete.isComplete = True

            # jobtomarkcomplete.(id=job_id)

            

            # print("this is marked complete " + str(job_id) + " " + jobtomarkcomplete.title) 

    return redirect(reverse('ijosephapp:yourjob'))