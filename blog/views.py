from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def startingPage(request):
    return render(request,'blog/index.html')

def posts(request):
        return render(request,'blog/all-posts.html')

def postDetails(request, slug):
    return HttpResponse(f"Details for post: {slug}")