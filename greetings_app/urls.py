from django.urls import path, include
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('loginpage/',views.loginpage,name='loginpage'),
   path('signup/',views.signuppage,name='signup'),
   path('register/',views.UserRegister,name='register'),
   path('loginuser/',views.UserLogin, name='login'),
   path('loggedout/',views.Userlogout, name='logout'),
]