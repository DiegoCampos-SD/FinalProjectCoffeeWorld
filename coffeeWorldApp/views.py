from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Drink, Bean
from .forms import DrinkForm, BeanForm
from django.shortcuts import render, redirect

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
            return ("ok")
    else:
        form = DrinkForm()
    return ("ok")

def bean_list(request):
    beans = Bean.objects.filter(creationDate__lte=timezone.now()).order_by('creationDate')
    return render(request, 'coffeeWorld/beans_list.html',{'bean':beans})

def bean_new(request):
    if request.method == "POST":
        form = BeanForm(request.POST)
        if form.is_valid():
            bean = form.save(commit=False)
            bean.author = request.user
            bean.creationDate = timezone.now()
            bean.save()
            return ("ok")
    else:
        form = BeanForm()
    return ("ok")
    
def create_order(request):
    if request.method == 'POST':
        
        return redirect('order_confirmation')
    

    return render(request, 'coffeeWorld/drink_list.html', {'drinks': drinks})

def order_confirmation(request):
    return render(request, 'coffeeWorld/order_confirmation.html')
