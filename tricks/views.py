from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView

from .models import CodeTrick, CodeTrickCreateForm

def index(request):
    return render(request, 'tricks/list.html', { 'tricks': CodeTrick.objects.all().order_by('-create_date') })

class CodeTrickCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'tricks/new.html', {'form': CodeTrickCreateForm()})

    def post(self, request, *args, **kwargs):
        form = CodeTrickCreateForm(request.POST)
        if form.is_valid():
            code_trick = form.save()
            code_trick.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'tricks/new.html', {'form': form})