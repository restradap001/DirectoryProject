from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from .views import HomeView, RegisterView, RestaurantListView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView

app_name = 'base'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(template_name='base/users/login.html'), name='login'),
    path('users/logout/', LogoutView.as_view(), name='logout'),

    path('restaurants/', RestaurantListView.as_view(), name='restaurants'),
    path('restaurants/create/', RestaurantCreateView.as_view(), name='create-restaurant'),
    path('restaurant/<int:pk>/update/', RestaurantUpdateView.as_view(), name='update-restaurant'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='delete-restaurant'),
]