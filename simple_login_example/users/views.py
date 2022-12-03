from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from users.models import User
import json
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def login(request: HttpRequest):
    context = {
        'method': request.method,
        'is_valid': True
    }

    if request.method == 'GET':
        return render(request, 'users/login.html', context)

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username, password=password)
            responce = redirect('pages:index')
            
            responce.set_cookie('username', user.username)
            responce.set_cookie('password', user.password)
            responce.set_cookie('is_login', True)

            return responce
        except User.DoesNotExist:  # 회원 정보가 없는 경우
            context['is_valid'] = False
            return render(request, 'users/login.html', context)
        
        

        


def login_detail(request: HttpRequest, id):
    return HttpResponse(f"user id는 {id}입니다.")

def index(request):
    return render(request, 'index.html')

def logout(request):
    response = redirect('pages:index')
    response.delete_cookie('is_login')
    response.delete_cookie('username')
    response.delete_cookie('password')

    return response

def signup(request):
    context = {
        'blank': False,
        'exist': False
    }

    template_name = 'users/signup.html'

    if request.method == "GET":
        return render(request, template_name, context)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # 빈칸 여부 확인
        if username == '' or password == '':
            context['blank'] = True
            return render(request, template_name, context)
        
        
        exist = User.objects.filter(username=username).exists()
        if exist: # 아이디가 이미 존재할때
            context['exist'] = exist
            return render(request, template_name, context)


        User.objects.create(username=username, password=password)
        return redirect('users:login')

    
