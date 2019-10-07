from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import CodeTrick, CodeTrickForm

class CodeTrickListView(ListView):
    model = CodeTrick
    template_name = 'tricks/list.html'
    paginate_by = 4

class CodeTrickCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'tricks/new.html', {'form': CodeTrickForm()})

    def post(self, request, *args, **kwargs):
        form = CodeTrickForm(request.POST)
        if form.is_valid():
            code_trick = form.save()
            code_trick.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'tricks/new.html', {'form': form})