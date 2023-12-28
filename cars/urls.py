from django.urls import path

from cars import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('add_car/', views.AddCarView.as_view(), name='add_car'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('all_cars/', views.AllCarsView.as_view(), name='all_cars'),
    path('car_detail/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('car_brand/', views.CarBrandListView.as_view(), name='car_brand'),
]
