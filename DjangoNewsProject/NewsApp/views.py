from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsModal
from .forms import NewsForm
from django.contrib import messages

def news_list(request):
    news = NewsModal.objects.all()
    return render(request, 'All_News.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(NewsModal, pk=pk)
    return render(request, 'NewsDetail.html', {'news': news})

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            messages.success(request, 'News Article Created Successfully.')
            return redirect('news-detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news_form.html', context={'form': form})

def news_edit(request, pk):
    news = get_object_or_404(NewsModal, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save()
            messages.success(request, 'News Article Updated Successfully.')
            return redirect('news-detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_form.html', {'form': form})

def news_delete(request, pk):
    news = get_object_or_404(NewsModal, pk=pk)
    news.delete()
    messages.success(request, 'News Article Deleted Successfully.')
    return redirect('news-home')

def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response