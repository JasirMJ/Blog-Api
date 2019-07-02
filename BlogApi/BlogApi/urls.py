"""BlogApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from blog import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'showPosts', views.PostViewSet)
router.register(r'showPostsDesc', views.PostDescViewSet)
router.register(r'tag', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addPost/', views.AddPost.as_view(), name='addPost'),
    path('showPostsById/',views.ShowPostById.as_view(),name="showPostById"),
    path('showPostsByTagId/',views.ShowPostByTagId.as_view(),name="showPostByTagId"),
    path('findPost/',views.FindPosts.as_view(),name="findPost"),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
