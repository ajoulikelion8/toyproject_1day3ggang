from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'content/mainpage.html')

def wholelist(request):
    return render(request,'content/wholelist.html')

def create(request):
    return render(request,'content/create.html')

def update(request):
    return render(request,'content/update.html')

def detail(request):
    return render(request,'content/detail.html')

def aboutus(request):
    return render(request,'content/aboutus.html')

