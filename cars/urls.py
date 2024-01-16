from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from cars import views

urlpatterns = [
                  path('', views.IndexView.as_view(), name='index'),
                  path('contacts/', views.ContactsView.as_view(), name='contacts'),
                  path('about/', views.AboutView.as_view(), name='about'),
                  path('all_cars/', views.AllCarsView.as_view(), name='all_cars'),
                  path('car_detail/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
                  path('car_brand/', views.CarBrandListView.as_view(), name='car_brand'),
                  path('create/', views.CarCreateView.as_view(), name='car_create'),
                  path('update/<int:pk>/', views.CarUpdateView.as_view(), name='car_update'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
