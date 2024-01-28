from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    # news_list = News.objects.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, 'news/single_page.html', context)

def homePageView(request):
    news_list = News.published.all().order_by('-published_time')[:15]
    categories = Category.objects.all()
    local_one = News.published.all().filter(category__name='Mahalliy').order_by('-published_time')[:1]
    local_news = News.published.all().filter(category__name='Mahalliy').order_by('-published_time')[1:6]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news,
        'local_one': local_one,
    }
    return render(request, 'news/index.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-published_time')[:15]
        context['mahalliy_xabarlar'] = News.published.all().filter(category__name='Mahalliy').order_by('-published_time')[:5]
        context['sport_xabarlar'] = News.published.all().filter(category__name='Sport').order_by('-published_time')[:5]
        context['xorij_xabarlar'] = News.published.all().filter(category__name='Xorij').order_by('-published_time')[:5]
        context['texnalogiya_xabarlar'] = News.published.all().filter(category__name='Texnalogiya').order_by('-published_time')[:5]

        return context


def contactPageViews(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>Biz bilan bog'langaningiz uchun rahmat!</h2>")
    context = {
        "form": form
    }

    return render(request, 'news/contact.html', context)


class LocalPageView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news

class ForeignPageView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news


class TecnologyPageView(ListView):
    model = News
    template_name = 'news/texnalogiya.html'
    context_object_name = 'texnalogiya_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnalogiya')
        return news


class SportPageView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news


def categoriesPageViews(request):
    context = {

    }
    return render(request, 'news/category.html', context)


def singlePageViews(request):
    context = {

    }
    return render(request, 'news/single.html', context)


def page404(request):
    context = {

    }
    return render(request, 'news/404.html', context)