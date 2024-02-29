from django.urls import path 
from .views import HomePageView, UserIndexView, UserShowView, UserCreateView, UserCreatedPageView, DeleteUserView

urlpatterns = [ 

    path('', HomePageView.as_view(), name='home'),
    path('users/', UserIndexView.as_view(), name='index'),
    path('users/create', UserCreateView.as_view(), name='form'),
    path('users/<str:id>', UserShowView.as_view(), name='show'),
    path('created', UserCreatedPageView.as_view(), name='created'),
    path('users/<str:id>/delete', DeleteUserView.as_view(), name='user_delete'),

] 