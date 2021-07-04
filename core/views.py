from django.shortcuts import render,redirect 
from core.forms import watchlistForm
from core.models import watchlist
def home(request):
    form = watchlistForm() 
    lists = watchlist.objects.all()
    if request.method == 'POST':
        form = watchlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mywatchlist')
    return render(request,'home.html',{'form' : form, 'lists' : lists})

def update(request, list_id): 
    list=watchlist.objects.get(id=list_id)
    form = watchlistForm(instance=list)
    if request.method == 'POST':
         form = watchlistForm(request.POST, instance=list)
         if form.is_valid():
            form.save()
            return redirect('mywatchlist')
    return render(request, 'update.html',{'form' : form})

def delete(request, list_id): 
    if request.method == 'POST':
        watchlist.objects.get(id=list_id).delete()
        return redirect('mywatchlist')
    
def mywatchlist(request):
    lists = watchlist.objects.all()
    return render(request,'mywatchlist.html',{'lists' : lists})