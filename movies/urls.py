from django.urls import path

from . import views

app_name = 'movie'
urlpatterns = [
path('', views.index, name='index'),
path('', views.all, name='all'),
path('', views.myrank, name='myrank'),
path('', views.show, name='show'),
path('edit_movie/<int:movie_id>', views.edit_movie, name='edit_movie')
]