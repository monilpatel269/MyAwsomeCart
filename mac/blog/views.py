from math import ceil
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from .models import Blogpost, Contact

# Create your views here.

def index(request):
    myposts= Blogpost.objects.all()
    return render(request, 'blog/index.html', {'myposts': myposts})

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html',{'post':post})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    thank=False
    if request.method =="POST":
     name=request.POST.get('name','')
     email=request.POST.get('email','')
     phone=request.POST.get('phone','')
     desc=request.POST.get('desc','')
     contact = Contact(name=name,email=email,phone=phone,desc=desc)
     contact.save()
     thank=True
    return render(request,'blog/contact.html',{'thank':thank})

def search(request):
    query= request.GET['search']
    if len(query)>78:
        allPosts=Blogpost.objects.none()
    else:
        allPostsTitle= Blogpost.objects.filter(title=query)
        allPostsAuthor= Blogpost.objects.filter(author=query)
        allPostsContent =Blogpost.objects.filter(content=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'blog/search.html', params)

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['firstName']
        lname=request.POST['lastName']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('blogHome')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('blogHome')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('blogHome')
         
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('blogHome')

    else:
        return HttpResponse("404 - Not found")

def handleLogIn(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("blogHome")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("blogHome")

    return HttpResponse("404- Not found")

def handleLogOut(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('blogHome')
