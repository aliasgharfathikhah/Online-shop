from django.urls import path
from item import views

urlpatterns = [
    path('new_item/', views.AddNewItme, name='addnewitem'),
    path('detail/<int:pk>/', views.ItemDetail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.EditItme, name='edit'),
]