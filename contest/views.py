from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Contest
# Create your views here.

class ContestList(ListView):
    model = Contest
    template_name = 'contest_list.html'

class DetailContest(DetailView):
    model = Contest
    template_name = 'detail_contest.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailContest,self).get_context_data(*args, **kwargs)
        return context