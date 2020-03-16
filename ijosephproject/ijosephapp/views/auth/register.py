from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User

def register_user(request):
    """View method for handling creation of a new user for auth
        Args:
        request = full http object
    """

    # For handling when user submits the form data
    if request.method == "POST":

        # First create a new user using django's built in craziness. create_user is a method in django.
        new_user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )

        # Second, make a librarian after the user has been created
        # librarian = Librarian.objects.create(
        #     user=new_user,
        #     # If you have other form data to save on the new librarian, that isn't a property of the User model...
        #     fave_color=request.POST['fave_color']
        # )

        login(request, new_user)

        # Redirect the browser to wherever you want to go after registering
        return redirect(reverse('ijosephapp:jobs'))

    # handles a request to load the empty form for the useer to fill out
    else:
        template = 'registration/register.html'

    return render(request, template, {})