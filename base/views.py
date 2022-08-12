from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Restaurant
from .forms import CustomUserCreationForm, RestaurantForm


class HomeView(TemplateView):
    template_name = 'base/index.html'


@method_decorator(user_passes_test(lambda u: not u.is_authenticated, login_url='base:home'), name='dispatch')
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('base:login')
    template_name = 'base/users/register.html'


@method_decorator(login_required(login_url='base:login'), name='dispatch')
class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'base/restaurants/create.html'
    success_url = reverse_lazy('base:restaurants')


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'base/restaurants/directory.html'
    context_object_name = 'restaurants'


@method_decorator(login_required(login_url='base:login'), name='dispatch')
class RestaurantUpdateView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'base/restaurants/update.html'
    success_url = reverse_lazy('base:restaurants')


@method_decorator(login_required(login_url='base:login'), name='dispatch')
class RestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('base:restaurants')
