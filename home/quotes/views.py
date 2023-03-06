from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Quotes, Authors
from .forms import QuoteForm, AuthorsForm
import itertools

def main(request):
    quotes_list = Quotes.objects.all()
    paginator = Paginator(quotes_list, 10)
    page = request.GET.get('page')
    text = 'Main'
    quotes = paginator.get_page(page)
    return render(request, 'quotes/index.html', {'quotes': quotes, 'text': text})


def create_quote(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
    return render(request, 'quotes/create_quote.html', context={'form': form})

def create_author(request):
    form = AuthorsForm()
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
    return render(request, 'quotes/create_author.html', context={'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Authors, author_id=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})

def details(request, quote_id):
    quote = get_object_or_404(Quotes, quote_id=quote_id)
    quote.tags = tags_list_to_str(quote.tags)
    return render(request, 'quotes/details.html', {'quote': quote})

def delete_quote(request, quote_id):
    Quotes.objects.get(pk=quote_id).delete()
    return redirect(to='quotes:main')


def tags_list_to_str(tags):
    if len(tags) >= 1:
        tags = ', '.join(tags)
    elif len(tags) == 1:
        tags = tags[0]
    return tags

def search_in_tags(request, tag):
    quotes = Quotes.objects.filter(tags__icontains=tag)
    text = f'Search by "{tag}"'
    return render(request, 'quotes/index.html', {'quotes': quotes, 'text': text})


def top_ten_tags(request):
    tags = Quotes.objects.values_list('tags', flat=True)
    tags_list = list(itertools.chain.from_iterable(tags))
    tags_set = set(tags_list)
    result = []
    for tag in tags_set:
        count = tags_list.count(tag)
        result.append([tag, count])
    tags = sorted(result, key=lambda x: x[1], reverse=True)[:10]
    print(tags)
    return render(request, 'quotes/top_ten_tags.html', {'tags': tags})