from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Showroom


class ShowroomListView(ListView):
    template_name = "showroom/list_car.html"
    model = Showroom


class ShowroomDetailView(DetailView):
    template_name = "showroom/detail_car.html"
    model = Showroom


class ShowroomCreateView(CreateView):
    template_name = "showroom/add_car.html"
    model = Showroom
    fields = ['manafactor','purchaser','desc']
    success_url = reverse_lazy("list_car")

class ShowroomUpdateView(UpdateView):
    template_name = "showroom/update_car.html"
    model = Showroom
    fields = ['manafactor','purchaser','desc']


class ShowroomDeleteView(DeleteView):
    template_name = "showroom/delete_car.html"
    model = Showroom
    success_url = reverse_lazy("list_car")