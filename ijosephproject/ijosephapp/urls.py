from ijosephapp.views import *
from django.urls import include, path
# from django.urls import path

app_name = "ijosephapp"

urlpatterns = [
    path('', home, name='home'),
    path('jobs/', job_list, name='jobs'),
]

# from django.urls import path
# from .views import *

# app_name = "libraryapp"

# urlpatterns = [
#     path('', book_list, name='home'),
#     path('books/', book_list, name='books'),
# ]
