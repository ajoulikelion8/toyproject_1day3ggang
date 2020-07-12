from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate
from account.models import MyUser

# Create your views here.


def login(request):
    return render(request, 'account/login.html')


def logincheck(request):
    if request.method == 'POST':
        print("request"+str(request))
        print("body"+str(request.body))
        username = request.POST.get('userid', '')
        userpassword = request.POST.get('userpw', '')
        print("userid="+username+"userpw="+userpassword)
        login_result = authenticate(username=username)

        print("result"+str(login_result))
        if login_result:
            return HttpResponse(status=200)
        else:
            return render(request, 'account/login.html', status=401)

    return HttpResponse(status=200)


def signup(request):
    return render(request, 'account/signup.html')


def signupcheck(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        mes_data = {}
        if not (username and password1 and password2):
            mes_data['error'] = "모든값을 입력하세요."
        if password1 != password2:
            mes_data['error'] = "비밀번호가 다릅니다."
        else:
            user = MyUser(user_name=username, password=password1)
            user.save()
            print("request"+str(request))
            print("request body :" + str(request.body))
            return render(request, 'account/login.html', mes_data)


def logout(request):
    return render(request, 'account/logout.html')
