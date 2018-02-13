from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.

#function will fire when the user want to signup
def signup(request):
    if request.method=='POST':
       form=UserCreationForm(request.POST)
       if form.is_valid():
          user=form.save() #form.save return a user that we have saved in our database  
          login(request,user) 
          return redirect('arti:arti')
    else:  
       form=UserCreationForm()
    return render(request,'accounts/temp.html',{'form':form})

#function will fire when the user want to log in 
def log(request):
    if request.method=='POST':
       form=AuthenticationForm(data=request.POST)    
       if form.is_valid():
            user=form.get_user()  #take the user data filled in thr form and trasfer into the user
            login(request,user)  #retrieve
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('arti:arti')            
    else:
       form=AuthenticationForm()

    return render(request,'accounts/temp2.html',{'form':form})
# function will fire when the user want to logout
def log2(request):
    if request.method=='POST':
       logout(request)# do not need to specify which user need to be loged out because djanco know the current user to be loged out
       return redirect('arti:arti')
