from django.urls import path
from .views import CategoryNewsView,HomeView,SearchView
urlpatterns = [
    path('category/<str:category>', CategoryNewsView.as_view(),name="category_news"),
    path('', HomeView.as_view(),name="home"),
    path('search/', SearchView.as_view(),name="search"),
   
]
