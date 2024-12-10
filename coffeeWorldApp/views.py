from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Drink
from .forms import DrinkForm, BeanForm

# Create your views here.
def drink_list(request):
    drinks = Drink.objects.filter(creationDate__lte=timezone.now()).order_by('creationDate')
    return render(request, 'coffeeWorld/drinks_list.html',{'drinks':drinks})

def drink_edit(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    return render(request, 'coffeeWorld/drink_detail.html', {'drinks':drinks})

def drink_new(request):
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            drink = form.save(commit=False)
            drink.author = request.user
            drink.creationDate = timezone.now()
            drink.save()
            return redirect('drink_detail', pk=drink.pk)
    else:
        form = DrinkForm()
    return render(request, 'coffeeWorld/drink_edit.html',{'form': form})

def drink_edit(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == "POST":
        form = DrinkForm(request.POST, instance=drink)
        if form.is_valid():
            drink = form.save(commit=False)
            drink.author = request.user        
            drink.save()
            return redirect('drink_detail', pk=drink.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
def bean_new(request):
    if request.method == "POST":
        form = BeanForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.creationDate = timezone.now()
            post.save()
            return ("ok")
    else:
        form = BeanForm()
    return ("ok")
