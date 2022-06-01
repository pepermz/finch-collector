from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Finch
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"
    



class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["finches"] = Finch.objects.all()
            # default header for not searching 
            context["header"] = "Trending Finches"
        return context


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'bio', 'verified_bird']
    template_name = "finch_create.html"
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'bio', 'verified_bird']
    template_name = "finch_update.html"
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete_confirmation.html"
    success_url = "/finches/"

# class FinchDetail(DetailView):
#     model = Finch
#     template_name = "finch_detail.html"