"""config URL Configuration

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
    2. Add a URL to urlpatterns:  path('config/', include('config.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers

from blog.apps.post import views as post_views
from blog.apps.comment import views as comment_views
from blog.apps.tag import views as tag_views

router = routers.DefaultRouter()

router.register(r'post', post_views.PostViewSet)
router.register(r'post_tag', post_views.PostTagViewSet)
router.register(r'post_vote', post_views.PostVoteViewSet)

router.register(r'comment', comment_views.CommentViewSet)

router.register(r'tag', tag_views.TagViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.apps.index.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
