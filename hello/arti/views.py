from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from .models import Articles
from django.contrib.auth.decorators import login_required 
from .import forms

def arti(request):
    articles=Articles.objects.all().order_by('date')
    return render(request,'arti/arpit.html',{'article':articles})
def details(request,slug):
    return HttpResponse(slug)

#decorator add additional functionality to the funtion (here the decorator is the login_url)

@login_required(login_url="/accounts/log")
#this statement will prevent the user to not access the create funtion if the user is not logged in and the redirect the user to make login and redirect to the login page
def create(request):
    if request.method=='POST':
       form=forms.CreateArticle(request.POST,request.FILES) #when we uplooad the files they do not come with the request object but they come with the seperate object  files on the request object @request.FILES
       if form.is_valid():
          instance=form.save(commit=False) # here commit = false is doing an action which tells that dont instantly save the changes to the databse but wait we wanted to do something with the instance variable 
          instance.author=request.user#now we are saving the current user that is logined in the instance of the form attach the article with the user
          instance.save()# now saving the changes
          return redirect('arti:arti')
    else:
       form=forms.CreateArticle()
    return render(request,'arti/create.html',{'form':form})


