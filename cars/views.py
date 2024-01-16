from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from cars.forms import CarForm
from cars.models import Car_brand, Car
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'
    queryset = Car.objects.all()[:3]


class ContactsView(ListView):
    template_name = 'cars/contacts.html'
    queryset = []

    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name')
        phone = self.request.POST.get('phone')
        message = self.request.POST.get('message')
        print(name, phone, message)
        return render(request, self.template_name, {'name': name, 'phone': phone, 'message': message})


class AboutView(ListView):
    template_name = 'cars/about.html'
    queryset = []


class AllCarsView(ListView):
    model = Car
    template_name = 'cars/all_cars.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'


class CarBrandListView(ListView):
    model = Car_brand
    template_name = 'cars/car_brand.html'
    context_object_name = 'car_brand_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('index')


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('index')
