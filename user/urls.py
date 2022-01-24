from django.urls import path
from user import views

app_name = 'user'

urlpatterns =[
    path('register/',views.sign_up,name='register'),
    path('signin/',views.sign_in,name ='login'),
    path('logout/',views.logout_user,name='logout'),

]