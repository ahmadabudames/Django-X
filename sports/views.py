from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import sports
# Create your views here.


class sportsListView(ListView):
    model= sports
    template_name = "sports_list.html"
    context_object_name='sports'



class sportsDetailView(DetailView):
    model=sports 
    template_name='sports_detail.html'



class sportsCreateView(CreateView):
    model= sports
    template_name='sports_create.html'
    fields=['title_field' ,'purchaser_field','description_field']
    success_url='/'

class sportsUpdateView(UpdateView):
    model=sports
    template_name='sports_update.html'  
    fields=['title_field' ,'purchaser_field','description_field']

class sportsDeleteView(DeleteView):
    model=sports
    template_name='sports_delete.html'  
    success_url= reverse_lazy('sports_list')
