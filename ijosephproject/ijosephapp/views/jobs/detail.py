import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ijosephapp.models import Job
from ..connection import Connection


def get_job(job_id):
      
    return Job.objects.get(pk=job_id)


@login_required
def job_details(request, job_id):
    if request.method == 'GET':
        job = get_job(job_id)
        template_name = 'jobs/detail.html'
        return render(request, template_name, {'job': job})

    elif request.method == 'POST':
        form_data = request.POST
        isCompleted = form_data.get("isCompleted", False)

        # Check if this POST is for editing a job
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):   
            # # retrieve it first:
            job_to_update = Job.objects.get(pk=job_id)

            # # Reassign a property's value
            job_to_update.title = form_data['title']
            job_to_update.category_id = form_data['category']
            job_to_update.location = form_data['location']
            job_to_update.description = form_data['description']
            isCompleted = isCompleted,
            user_id = request.user.id

            # # Save the change to the db
            job_to_update.save()

            return redirect(reverse('ijosephapp:jobs'))

        # Check if this POST is for deleting a job
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            job = Job.objects.get(pk=job_id)
            job.delete()

            return redirect(reverse('ijosephapp:jobs'))