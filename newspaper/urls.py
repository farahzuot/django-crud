from django.urls import path,include
from .views import HomeView,DetailedView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('<int:pk>/', DetailedView.as_view(), name = 'details'),
    path('new/', BlogCreateView.as_view(), name = 'add'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name = 'delete')

]
