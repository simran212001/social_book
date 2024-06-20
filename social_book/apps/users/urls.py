from django.urls import path
from .import views

from django.urls import include, re_path


users_urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dashboard1/',views.dashboard1,name = 'dashboard1'),
    path('registered_user/',views.registered_user,name='registered_user'),
    path('upload_books/',views.upload_books,name='upload_books'),
    path('book_details/',views.book_details,name='book_details'),


    path('profile/',views.profile,name='profile'),
   
    

]