from django.urls import path
from . import views

urlpatterns = [
    # Actor URLs
    path('actors/', views.actor_list),
    path('actors/<int:pk>/', views.actor_detail),

    # Director URLs
    path('directors/', views.director_list),
    path('directors/<int:pk>/', views.director_detail),

    # Movie URLs
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
]
