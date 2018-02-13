from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    #return HttpResponse('about')
     return render(request,'par.html')
    #return HttpResponse('this is your first html rendering')
def main(request):
     return render(request,'new.html')
