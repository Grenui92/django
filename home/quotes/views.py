from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quotes, Authors
from .forms import QuoteForm, AuthorsForm


def main(request):
    quotes = Quotes.objects.all()
    for quote in quotes:
        quote.tags = tags_list_to_str(quote.tags)
    return render(request, 'quotes/index.html', {'quotes': quotes})


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