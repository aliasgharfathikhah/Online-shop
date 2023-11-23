from django.urls import path
from core import views
from django.contrib.auth import views as auth_views
from core.forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('category_search/<str:categorys>', views.category_search, name='category search'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
