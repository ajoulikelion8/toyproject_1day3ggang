from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .forms import PostForm,UpdateForm
from content.models import Todolist
from account.models import User

# Create your views here.
def mainpage(request):
    return render(request,'content/mainpage.html')

def wholelist(request):
    lists = Todolist.objects
    return render(request,'content/wholelist.html',{'lists':lists})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wholelist')
        
    else:
        form = PostForm()
        return render(request,'content/create.html',{'form':form})

def delete(request,list_id):
    lists = Todolist.objects.get(pk=list_id)
    lists.delete()
    return redirect('wholelist')

def update(request,list_id):
    obj=get_object_or_404(Todolist,pk=list_id)
    if request.method == 'POST':
        form = UpdateForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('wholelist')
        
    else:
        form = PostForm()
        return render(request,'content/update.html',{'form':form,'obj':obj})


def detail(request,list_id):
    list_detail = get_object_or_404(Todolist,pk=list_id)
    return render(request,'content/detail.html',{'list':list_detail})

def aboutus(request):
    return render(request,'content/aboutus.html')

