import sqlite3
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from ijosephapp.models import Job
from ijosephapp.models import JobCategory
from ijosephapp.models import model_factory
from ..connection import Connection


def get_categories():
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(JobCategory)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     select
    #         c.id,
    #         c.category
    #     from ijosephapp_jobcategory c
    #     """)

    #     return db_cursor.fetchall()

    all_categories = JobCategory.objects.all()
    return all_categories
    

@login_required 
def job_form(request):
    if request.method == 'GET':
        categories = get_categories()
        template = 'jobs/form.html'
        context = {
            'all_categories': categories    
        }

        return render(request, template, context)