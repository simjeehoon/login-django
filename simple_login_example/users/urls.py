from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/<int:id>/', views.login_detail, name='login-detail'),
    path('login/index', views.logout, name='index'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup')
]