from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Drink
from .forms import DrinkForm

# Create your views here.
def drink_list(request):
    drinks = Drink.objects.filter(creationDate__lte=timezone.now()).order_by('creationDate')
    return render(request, 'coffeeWorld/drinks_list.html',{'drinks':drinks})

def drink_new(request):
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.creationDate = timezone.now()
            post.save()
            return ("ok")
    else:
        form = CreationForm()
    return ("ok")
    