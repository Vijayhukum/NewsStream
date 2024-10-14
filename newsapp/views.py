from django.shortcuts import render
import requests
from django.views.generic import TemplateView,ListView
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage





def category_news_view(request, category):
    print(f"{category} came from view ")
    url = f'https://newsapi.org/v2/everything?q={category}&sortBy=publishedAt&apiKey={settings.NEWS_API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        articles = [
            article for article in articles
            if article['title'] != "[Removed]"
            and article.get('urlToImage') not in [None, 'null']
            and article['source']['name'] != "[Removed]"
        ]
    else:
        print(f'Failed to fetch news articles: {response.status_code}')
        articles = []

    paginator = Paginator(articles, 10)  # Show 10 articles per page
    page = request.GET.get('page')  # Get the current page number from the query parameters

    try:
        paginated_articles = paginator.page(page)
    except PageNotAnInteger:
        paginated_articles = paginator.page(1)  # If page is not an integer, deliver first page
    except EmptyPage:
        paginated_articles = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page

    context = {
        'articles': paginated_articles,
        'title': f'NewsStream - {category.title()} News',
        'current_category': category,
        'is_paginated': paginated_articles.has_other_pages(),
        'page_obj': paginated_articles,
        'paginator': paginator
    }

    return render(request, 'newsapp/category.html', context)


def home_view(request):
    url = f'https://newsapi.org/v2/everything?q=*&language=en&sortBy=publishedAt&apiKey={settings.NEWS_API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        articles = [article for article in articles if article['title'] != "[Removed]"]

        paginator = Paginator(articles, 10)
        page = request.GET.get('page')

        try:
            paginated_articles = paginator.page(page)
        except PageNotAnInteger:
            paginated_articles = paginator.page(1)
        except EmptyPage:
            paginated_articles = paginator.page(paginator.num_pages)

        context = {
            'articles': paginated_articles,
            'is_paginated': paginated_articles.has_other_pages(),
            'page_obj': paginated_articles,
            'paginator': paginator
        }
    else:
        context = {'articles': []}

    return render(request, 'newsapp/home.html', context)









def search_view(request):
    search_query = request.GET.get('query', '')
    articles = []

    if search_query:
        url = f'https://newsapi.org/v2/everything?q={search_query}&sortBy=publishedAt&language=en&apiKey={settings.NEWS_API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            articles = [
                article for article in articles
                if article['title'] != "[Removed]"
                and article.get('urlToImage') not in [None, 'null']
                and article['source']['name'] != "[Removed]"
            ]
        else:
            print(f'Failed to fetch news articles: {response.status_code}')

    context = {
        'articles': articles,
        'search_query': search_query,
    }

    return render(request, 'newsapp/search.html', context)
