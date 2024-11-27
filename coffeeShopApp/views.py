from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Drink
from .forms import DrinkForm

# Create your views here.
"""def drink_list(request):
    drinks = Drink.objects.filter(creationDate__lte=timezone.now()).order_by('creationDate')
    return render(request, 'coffeShop/drink_list.html',{'drinks':drinks})"""

"""def drink_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'coffeShop/drink_detail.html', {'drink': drink})"""

def drink_new(request):
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.creationDate = timezone.now()
            post.save()
            return ("ok")
            #return redirect('drink_detail', pk=drink.pk)
    else:
        form = CreationForm()
    return ("ok")
    #return render(request, 'coffeShop/drink_edit.html', {'form': form})

"""def drink_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = DrinkForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publishedDate = timezone.now()
            post.save()
            return redirect('post_detail', pk=drink.pk)
    else:
        form = CreationForm(instance=post)
    return render(request, 'coffeShop/drink_edit.html', {'form': form})"""