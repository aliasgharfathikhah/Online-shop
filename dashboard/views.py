from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items
    })


