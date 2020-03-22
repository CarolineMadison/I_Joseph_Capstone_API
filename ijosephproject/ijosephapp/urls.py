from ijosephapp.views import *
from django.urls import include, path
from .views import *
# from django.urls import path

app_name = "ijosephapp"

urlpatterns = [
    path('home/', home, name='home'),
    path('jobs/', job_list, name='jobs'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name='logout'),
    path('jobs/form/', job_form, name='job_form'),
    path('jobs/<int:job_id>/', job_details, name='job'),
    path('yourjobs/', yourjobs_list, name='yourjob'),
]