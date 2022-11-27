from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.LoginPage,name="loginpage"),
    path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
]
