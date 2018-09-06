from django.urls import path

from blog.apps.index.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index')
]
