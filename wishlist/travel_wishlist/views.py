from django.shortcuts import render, redirect, reverse
from django.conf.urls import url
from .models import Place
from .forms import NewPlaceForm

# Create your views here.
def place_list(request):
    # return render(request, 'travel_wishlist/wishlist.html')

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')



    places = Place.objects.filter(visited=False)
    form = NewPlaceForm()
    return render(request,'travel_wishlist/wishlist.html', {'places' : places})

def places_visited(request):

    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited':visited})

def place_is_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = Place.Objects.get(pk=pk)
        place.visited = True
        place.save()
    return redirect('place_list')
