from django.conf.urls import url
from campNowProjects import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'items/', views.ItemList.as_view()),
        #name=views.DogList.name),
    path(r'items/<int:pk>/', views.ItemDetail.as_view()),
        #name=views.DogDetail.name),
    path(r'users/', views.UserList.as_view()),
    path(r'users/<int:pk>/',views.UserDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

#''' url(r'^users/$',
    #    views.UserList.as_view(),
    #    name=views.UserList.name),
    #url(r'^users/(?P<pk>[0-9]+)/$',
    #    views.UserDetail.as_view(),
    #    name=views.UserDetail.name),'''
