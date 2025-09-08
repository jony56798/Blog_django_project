from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You are now logged in.")
            login(request, user)
            return redirect("post_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})
