from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
import json
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import os
# NEW ROUTES
import requests
import tempfile
from django.core import files


def home(request):
    return render(request, "home.html")


def pricing(request):
    if not request.user.is_authenticated:
        return render(request, "pricing.html")
    return redirect("home")


def about(request):
    return render(request, "about.html")


def hiw(request):
    return render(request, "hiw.html")


def my_account(request):
    if request.user.is_authenticated:
        return render(request, "my_account.html")


# def get_slides(request, project_id):
#     if request.user.is_authenticated or True:
#         print(request.user)
#         user = request.user
#         project = Project.objects.get(user=user, id=project_id)
#         slides = project.slides.values('id', 'slide_text', 'slide_visuals')
#         print(slides)
#         for slide in slides:
#             if slide['slide_visuals'] != None:
#                 slide['slide_visuals'] = list(project.slides.get(id=slide['id']).slide_visuals.values(
#                     'slide_visual', 'slide_visual_type'))
#         slides = json.loads(json.dumps(list(slides)))
#         return JsonResponse(slides, safe=False)
#         # return JsonResponse(json.dumps(slides.values()), safe=False)


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            try:
                name = request.POST["name"]
                username = request.POST["username"]
                email = request.POST["email"]
                password = request.POST["password"]
                try:
                    user = User.objects.get(email=email)
                    messages.error(
                        request, "An Account with this email already exists")
                    return redirect("/")
                except:
                    try:
                        user = User.objects.create_user(
                            username=username, email=email, password=password, first_name=name)
                        user.save()
                        user = authenticate(
                            username=username, password=password)
                        if user is not None:
                            login(request, user)
                            messages.success(request, "Welcome to Adwiti")
                            return redirect("dashboard")
                    except IntegrityError:
                        messages.error(
                            request, "Username Taken. Please try different username")
                        return redirect("/")
            except:
                messages.error(
                    request, "Please fill in these fields correctly")
                return redirect("/")
        return redirect("/")
    return redirect("/")


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            try:
                email = request.POST["email"]
                password = request.POST["password"]
                try:
                    username = User.objects.get(email=email).username
                    try:
                        user = authenticate(
                            username=username, password=password)
                        if user is not None:
                            login(request, user)
                            messages.success(request, "Welcome Back")
                            return redirect("dashboard")
                        else:
                            messages.error(
                                request, "Invalid Username and Password")
                            return redirect("/")
                    except:
                        messages.error(request, "Server Error")
                        return redirect("/")
                except:
                    messages.error(request, "Please Signup")
                    return redirect("/")
            except:
                messages.error(
                    request, "Please fill in all the fields correctly")
                return redirect("/")
        return redirect("/")
    return redirect("/")


def log_out(request):
    logout(request)
    return redirect("home")


def dashboard(request):
    try:
        user = projectUser.objects.get(user=request.user)
    except:
        user = projectUser.objects.create(user=request.user)

    projects = project.objects.filter(user=user)
    return render(request, "dashboard.html", {'data': projects})


def adwiti(request, user, project_name):
    if request.user.is_authenticated:
        user = projectUser.objects.get(user=request.user)
        proj = project.objects.get(user=user, name=project_name)
        proj = proj.slides.all()
        return render(request, "index.html", {'data': proj, 'project_name': project_name})


def projectStartAjax(request):
    if request.user.is_authenticated and request.method == "POST":
        name = request.POST['name']
        user = projectUser.objects.get(user=request.user)
        try:
            project.objects.get(user=user, name=name)
            return JsonResponse({"exist": True})
        except:
            project.objects.create(
                user=user,
                name=name,
                # slides = slides,
            )
            data = {'user': str(request.user), 'p_name': name}

        return JsonResponse(data)


def addPPTAjax(request):
    user = projectUser.objects.get(user=request.user)
    proj = project.objects.get(user=user, name=request.POST['name'])
    # print(request.POST['data'])
    # for f in json.loads(request.POST['data']):
    #     print(f['FileName'])
    for f in json.loads(request.POST['data']):
        # Stream the image from the url
        response = requests.get(f['Url'], stream=True)

        # Was the request OK?
        if response.status_code != requests.codes.ok:
            # Nope, error handling, skip file etc etc etc
            continue

        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()

        # Read the streamed image in sections
        for block in response.iter_content(1024 * 8):

            # If no more file then stop
            if not block:
                break

            # Write image block to temporary file
            lf.write(block)

        # Create the model you want to save the image to
        sl = slide.objects.create(
            file_type="image",
            slide=None,
        )

        # Save the temporary image to the model#
        # This saves the model so be sure that it is valid
        sl.slide.save(f['FileName'], files.File(lf))
        proj.slides.add(sl)

    return JsonResponse({'data': json.loads(request.POST['data'])})


def addImgAjax(request):
    data = {}
    user = projectUser.objects.get(user=request.user)
    proj = project.objects.get(user=user, name=request.POST['name'])
    sl = slide.objects.create(
        file_type="image",
        slide=request.FILES['file'],
    )
    proj.slides.add(sl)
    return JsonResponse(data)


def addSlideAjax(request):
    data = {}
    user = projectUser.objects.get(user=request.user)
    proj = project.objects.get(user=user, name=request.POST['name'])
    i = 2
    for obj in proj.slides.all():
        obj.slide_text = request.POST['text'+str(i)]
        obj.save()
        i += 1

    return JsonResponse(data)


def update_info(request):
    if request.user.is_authenticated and request.method == "POST":
        try:
            name = request.POST["name"]
            email = request.POST["email"]
            emailExists = False
            try:
                user = User.objects.get(email=email)
                if (user.username != request.user.username):
                    emailExists = True
                    messages.error(
                        request, "An Account with this email already exists")
                    return redirect("my_account")
            except:
                pass
            finally:
                if not emailExists:
                    user = User.objects.get(username=request.user.username)
                    user.first_name = name
                    user.email = email
                    user.save()
                    messages.success(request, "Updated Successfully")
                    return redirect("my_account")
        except:
            messages.error(request, "Please fill in these fields correctly")
            return redirect("my_account")
    return redirect("my_account")


def change_password(request):
    if request.user.is_authenticated and request.method == "POST":
        try:
            c_pass = request.POST["current-password"]
            n_pass = request.POST["new-password"]
            try:
                user = User.objects.get(username=request.user.username)
                if user.check_password(c_pass):
                    user.set_password(n_pass)
                    user.save()
                    u = authenticate(username=user.username, password=n_pass)
                    if u is not None:
                        login(request, u)
                        messages.success(
                            request, "Password Changed successfully")
                        return redirect("my_account")
                    else:
                        print("why")
                        messages.error(request, "Server Error")
                        return redirect("my_account")
                else:
                    messages.error(request, "Current Password doesn't match")
                    return redirect("my_account")
            except:
                messages.error(request, "Server Error")
                return redirect("my_account")
        except:
            messages.error(request, "Please fill in these fields correctly")
            return redirect("my_account")
