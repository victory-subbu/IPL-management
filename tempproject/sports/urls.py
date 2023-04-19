from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('search/',views.search,name="search"),
    path('search1/',views.search1,name="search1"),
    path('search2',views.search2,name="search2"),
    path('search3/',views.search3,name='search3'),
    path('search4/',views.search4,name='search4'),
    path('search5/',views.search5,name='search5'),
    path('search6/',views.search6,name='search6'),
    path('search7/',views.search7,name='search7'),
    path('search8/',views.search8,name='search8'),
    path('search9/',views.search9,name='search9'),
    path('home/',views.home,name="home"),
    path('', views.index, name='index'),
    path("add_data/",views.add_data,name="add_data"),
    path("delete_data/<int:myid>/",views.delete_data,name="delete_data"),
    path("edit_data/<int:myid>/",views.edit_data,name="edit_data"),
    path("checkapi/",views.checkapi,name="checkapi"),
    path("postapi/",views.postapi,name="postapi"),
    path("updateapi/<int:id>/",views.updateapi,name="updateapi"),
    path("deleteapi/<int:id>/",views.deleteapi,name="deleteapi"),

    path("getclassbasedview/",views.PlayerslistGet.as_view()),
    path("createclassbasedview/",views.PlayerslistCreate.as_view()),




    



]