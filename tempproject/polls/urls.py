from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('sanjay/shitij/',views.shitij,name="shitij"),
    path('auth/', views.auth, name='auth'),
    path('auth/log/',views.login,name='login'),
    path('testlogin/',views.testlogin,name="testlogin"),
    path('',views.templogin,name="templogin"),
 
    #path('home/',views.home,name="home"),
    path('ssession',views.setsession),  
    path('gsession',views.getsession),

]