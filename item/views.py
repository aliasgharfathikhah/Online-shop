from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from item.forms import NewItem, EditItem

def ItemDetail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_item': related_item,
        'created_by': item.created_by,
    })


@login_required
def AddNewItme(request):
    if request.method == 'POST':
        form = NewItem(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItem()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item'
    })

@login_required
def EditItme(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItem(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
    else:
        form = EditItem(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'eidt item'
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard/indax.html1')