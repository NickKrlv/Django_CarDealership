from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path

from cars import views

urlpatterns = [
                  path('', views.IndexView.as_view(), name='index'),
                  path('contacts/', views.ContactsView.as_view(), name='contacts'),
                  path('about/', views.AboutView.as_view(), name='about'),
                  path('all_cars/', views.AllCarsView.as_view(), name='all_cars'),
                  path('car_detail/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
                  path('car_brand/', views.CarBrandListView.as_view(), name='car_brand'),
                  path('create/', login_required(views.CarCreateView.as_view()), name='car_create'),
                  path('update/<int:pk>/', login_required(views.CarUpdateView.as_view()), name='car_update'),
                  path('version_create/', views.VersionCreateView.as_view(), name='version_create'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
