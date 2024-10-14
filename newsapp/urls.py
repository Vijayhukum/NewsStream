from django.urls import path
from .views import category_news_view,home_view,search_view
urlpatterns = [
    path('category/<str:category>', category_news_view,name="category_news"),
    path('', home_view,name="home"),
    path('search/', search_view,name="search"),
   
]
