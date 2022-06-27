
from django.urls import path

from . import views
from rest_framework import renderers

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path('api/posts/', post_list, name='post-list'),
    path('api/posts/<int:pk>/', post_detail, name='post-detail'),

]
