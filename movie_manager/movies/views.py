from django.shortcuts import render
from . models import movie_info
from . forms import movie_form
# Create your views here.
def create(request):
    if request.POST :
        frm=movie_form(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm=movie_form()



        
    return render(request, 'create.html', {'frm':frm})

def edit(request):
    return render(request, 'edit.html')

def list(request):
     movies_data = movie_info.objects.all()
     print(movies_data)
     return render(request, 'list.html', {'movies': movies_data})