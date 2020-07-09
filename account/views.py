from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == "post":
        id = request.post['id']
        password = request.post['password']
        user = auth.authenticate(request, id=id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else:
            return render(request,'account/login.html', {'error': 'id or password is incorrect'})
    else:
        return render(request,'account/login.html')

def signup(request):
    if request.method == "post":
        if request.post["password1"] == request.post["password2"]:
            user =User.objects.create_user(
                username=request.post["username"],id=request.post["id"],password=request.post["password1"])
            auth.login(request,user)
            return redirect('mainpage')
    return render(request,'account/signup.html')

def logout(request):
    return render(request,'account/logout.html')
    
    

