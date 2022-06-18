from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videogames/', views.videogames, name='videogames'),
    path('videogamedetail/<int:id>', views.videogamedetail, name='detail'),
    path('videogamereview/<int:id>', views.vgreview, name='review'),
    path('addvideogame/', views.addvideogame, name='addvideogame'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path('addreview/<int:id>', views.addreview, name='addreview'),
]
