import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ijosephapp.models import Job
from ..connection import Connection


def get_job(job_id):
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Book)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         b.id,
    #         b.title,
    #         b.isbn,
    #         b.author,
    #         b.year,
    #         b.librarian_id,
    #         b.location_id
    #     FROM libraryapp_book b
    #     WHERE b.id = ?
    #     """, (book_id,))

    #     return db_cursor.fetchone()
      
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

        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #     UPDATE libraryapp_book
            #     SET title = ?,
            #         author = ?,
            #         isbn = ?,
            #         year = ?, 
            #         location_id = ?
            #     WHERE id = ?
            #     """,
            #     (
            #         form_data['title'], form_data['author'],
            #         form_data['isbn'], form_data['year_published'],
            #         form_data["location"], book_id,
            #     ))
                
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

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #         DELETE FROM libraryapp_book
            #         WHERE id = ?
            #     """, (book_id,))
                
            job = Job.objects.get(pk=job_id)
            job.delete()

            return redirect(reverse('ijosephapp:jobs'))