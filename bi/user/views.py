from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm


# Create your views here.
def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse('{}님 로그인 하셨습니다.'.format(str(user.username)))
    return HttpResponse('This is home')


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form})
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    #
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
    #
    #     res_data = dict()
    #     if not (username and password):
    #         res_data['error'] = '빈 입력 값이 있습니다.'
    #     else:
    #         user = User.objects.get(username=username)
    #
    #         if check_password(password, user.password):
    #             request.session['user'] = user.id
    #             return redirect('/')
    #         else :
    #             res_data['error'] = '비밀번호가 틀렸습니다.'
    #
    #
    #     return render(request, 'login.html', res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = dict()

        if not(username and useremail and password and re_password):
            res_data['error'] = '빈 입력 값이 있습니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password),
            )
            user.save()
            return redirect('/user/login')

        return render(request, 'register.html', res_data)





