from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Market
from .forms import MarketForm


class MarketFormView(View):
    def post(self, request):
        form = MarketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        context = {
            'form': form
        }
        return render(request, 'market/create_update.html', context)

    def get(self, request):
        form = MarketForm()
        context = {
            'form': form
        }
        return render(request, 'market/create_update.html', context)


class MarketListView(ListView):
    model = Market
    template_name = 'market/list.html'


class MarketDetailView(DetailView):
    model = Market
    template_name = 'market/detail.html'


class MarketDeleteView(DeleteView):
    model = Market
    success_url = reverse_lazy('list')
