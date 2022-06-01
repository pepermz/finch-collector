from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# import models
from .models import Finch
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"
    



class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finches"] = Finch.objects.all() # Here we are using the model to query the database for us.
        return context



# class ArtistList(TemplateView):
#     template_name = "artist_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         name = self.request.GET.get("name")
#         if name != None:
#             context["finch"] = Finch.objects.filter(name__icontains=name)
#             # We add a header context that includes the search param
#             context["header"] = f"Searching for {name}"
#         else:
#             context["finch"] = Finch.objects.all()
#             # default header for not searching 
#             context["header"] = "Trending Finch"
#         return context

# class FinchCreate(CreateView):
#     model = Finch
#     fields = ['name', 'img', 'bio', 'verified_finch']
#     template_name = "finch_create.html"
#     # this will get the pk from the route and redirect to artist view
#     def get_success_url(self):
#         return reverse('finch_detail', kwargs={'pk': self.object.pk})

# class FinchDetail(DetailView):
#     model = Finch
#     template_name = "finch_detail.html"