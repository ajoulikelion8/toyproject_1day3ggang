from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Todolist

# Create your views here.
def mainpage(request):
    return render(request,'content/mainpage.html')

def wholelist(request):
    lists = Todolist.objects
    return render(request,'content/wholelist.html',{'lists':lists})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        # if form.is_valid():
        post = form.save()
        # return redirect(post)
    else:
        form = PostForm()
        return render(request,'content/create.html',{'form':form})
    # form = PostForm()
    # return render(request,'content/create.html',{'form':form})

def update(request):
    return render(request,'content/update.html')

def detail(request):
    return render(request,'content/detail.html')

def aboutus(request):
    return render(request,'content/aboutus.html')

