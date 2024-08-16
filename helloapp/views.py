from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def print_hello(request):
    movies_data ={
        'movies': [
        {
        'title': 'godfather',
        'year': '1997',
        'summary': 'story of a under world king',
        'success': False,
        },
        {
        'title': 'Batman',
        'year': '2000',
        'summary': 'story of a unknownvhero',
        'success': True,
        },
        {
        'title': 'spiderman',
        'year': '2005',
        'summary': 'rise of a new star',
        'success': True,
        },
        {
        'title': 'redemption',
        'year': '1995',
        'summary': 'story of a prisnor',
        'success': False,
        },
        {
        'title': 'king',
        'year': '1997',
        'summary': '',
        'success': False,
        },

    ]}
    return render(request, 'hello.html', movies_data)
