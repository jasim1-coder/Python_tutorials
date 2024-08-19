from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST :
        print(request.POST.get ('title'))
        print(request.POST.get ('year'))

    return render(request, 'create.html')

def edit(request):
    return render(request, 'edit.html')

def list(request):
     movies_data ={
        'movies': [
        {
        'title': 'godfather',
        'year': '1997',
        'summary': 'story of a under world king',
        'success': False,
        'img':'godfather.jpg'
        },
        {
        'title': 'Batman',
        'year': '2000',
        'summary': 'story of a unknownvhero',
        'success': True,
        'img':'batman.jpg'
        },
        {
        'title': 'spiderman',
        'year': '2005',
        'summary': 'rise of a new star',
        'success': True,
        'img':'godfather.jpg'
        },
        {
        'title': 'redemption',
        'year': '1995',
        'summary': 'story of a prisnor',
        'success': False,
        'img':'redemtion.jpg'
        },
        {
        'title': 'king',
        'year': '1997',
        'summary': 'the story of a king and his castle ',
        'success': False,
        }

        ]}
     return render(request, 'list.html', movies_data)