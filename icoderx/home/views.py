from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import Contact, section
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here. 
def home(request):
    allposts=section.objects.all()
    context={'allpost':allposts}
    return render(request,'home/home.html',context)
def about(request):
    return render(request,"home/about.html")
def contact(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2  or len(phone)<5:
            messages.error(request,"bhosdike phie se  form bhar")
        else:
            obj=Contact(name=name,email=email,phone=phone,content=content)
            obj.save()
            messages.success(request,"your information has been sent successfully!")
    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    allpostauthor=Post.objects.filter(author__icontains=query) 
    allpostcontent=Post.objects.filter(content__icontains=query) 
    allpost=allpostauthor.union(allpostcontent)
    
    context={'allpost':allpost,'query':query}
    return render(request,'home/search.html',context)
    # return HttpResponse("search")

def handlesignup(request):
    if request.method =="POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.Last_name=lname
        myuser.save()
        messages.success(request,"your account is created successfull!")
        return redirect("/")
    else:
        return HttpResponse('not found')
    

def handlelogin(request):
    if request.method=="POST":
        loginusername= request.POST["loginusername"]
        loginpass= request.POST["loginpass"]
        user= authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request,"successfully loggedin")
            return redirect("/")
        else:
            messages.error(request,"invalid credential!")
            return redirect("/")
    return HttpResponse("logged in")

def handlelogout(request):
    logout(request)
    return redirect("/")
    