from django.urls import path
from . import views

urlpatterns = [
    path("",views.startingPage, name = 'starting-page'),
    path("posts",views.posts, name = 'posts'),
    path("posts/<slug>/", views.postDetails, name ='post-details')
]