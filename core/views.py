from django.shortcuts import render, redirect
from item.models import Category, Item
from core.forms import SignupForm

def index(request):
    item = Item.objects.filter(is_sold = False)
    category = Category.objects.all()

    return render(request, 'core/index.html', {
        'items': item,
        'categorys': category,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm

    return render(request, 'core/signup.html', {
        'form': form
    })