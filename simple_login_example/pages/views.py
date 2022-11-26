from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'is_login': False,
        'username': None,
        'password': None
    }
    
    is_login = request.COOKIES.get('is_login', False)
    if is_login:
        context['is_login'] = True
        context['username'] = request.COOKIES['username']
        context['password'] = request.COOKIES['password']

    return render(request, 'index.html', context)

