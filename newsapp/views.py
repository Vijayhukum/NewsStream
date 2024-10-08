from django.shortcuts import render
import requests
from django.views.generic import TemplateView,ListView
from django.conf import settings




class CategoryNewsView(TemplateView):
    template_name = 'newsapp/category.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category')
        print(f"{category} came from view ")
        url = f'https://newsapi.org/v2/everything?q={category}&sortBy=publishedAt&apiKey={settings.NEWS_API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            context['articles'] = data.get('articles', [])

            context['articles'] = [
            article for article in context['articles']
            if article['title'] != "[Removed]"
            and article.get('urlToImage') not in [None, 'null']
            and article['source']['name'] != "[Removed]"
            ]
        else:
            print(f'Failed to fetch news articles: {response.status_code}')
            context['articles'] = [] 
        context['title'] = f'NewsStream - {category.title()} News'
        context['current_category'] = category
        return context


class HomeView(TemplateView):
    template_name = 'newsapp/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = f'https://newsapi.org/v2/everything?q=*&language=en&sortBy=publishedAt&apiKey={settings.NEWS_API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            context['articles'] = data.get('articles', [])
            for article in context['articles']:
                if article['title'] == "[Removed]":
                    context['articles'].remove(article)
                    print("article removed")
        else:
            print(f'Failed to fetch news articles: {response.status_code}')

        return context
    




from django.conf import settings
from django.views.generic import ListView
import requests

class SearchView(ListView):
    template_name = 'newsapp/search.html'
    context_object_name = 'articles'  # Use this to simplify the template

    def get_queryset(self):
        # Return an empty list by default since we're fetching from an API
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('query', '')

        if search_query:
            context['search_query'] = search_query  # Retain query in form input
            news_api_key = settings.NEWS_API_KEY
            url = f'https://newsapi.org/v2/everything?q={search_query}&sortBy=publishedAt&language=en&apiKey={news_api_key}'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                
                # Filter articles based on your criteria
                context['articles'] = [
                    article for article in articles
                    if article['title'] != "[Removed]"
                    and article.get('urlToImage') not in [None, 'null']
                    and article['source']['name'] != "[Removed]"
                ]
            else:
                print(f'Failed to fetch news articles: {response.status_code}')
                context['articles'] = []

        return context 
