from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.


def login(request):
    return render(request, 'account/login.html')


def logincheck(request):
    if request.method == 'POST':
        print("request"+str(request))
        print("body"+str(request.body))
        #userid = request.POST.get('userid', '')
        #userpassword = request.POST.get('userpw', '')
        # print("userid="+userid+"userpw="+userpassword)
        #login_result = authenticate(user_id=userid, password=userpassword)

        # print("result"+str(login_result))
        # if login_result:
        # return HttpResponse(status=200)
        # else:
        # return render(request, 'account/login.html', status=401)

    return HttpResponse(status=200)


def signup(request):
    if request.method == "post":
        if request.post["password1"] == request.post["password2"]:
            user = User.objects.create_user(
                username=request.post["username"], id=request.post["id"], password=request.post["password1"])
            auth.login(request, user)
            return redirect('mainpage')
    return render(request, 'account/signup.html')


def logout(request):
    return render(request, 'account/logout.html')
