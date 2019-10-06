from django.shortcuts import render
from .models import CodeTrick, CodeTrickCreateForm
from django.views.generic.edit import CreateView
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'tricks/index.html', { 'tricks': CodeTrick.objects.all().order_by('-create_date') })

class CodeTrickCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'tricks/new.html', {'form': CodeTrickCreateForm()})

    def post(self, request, *args, **kwargs):
        form = CodeTrickCreateForm(request.POST)
        if form.is_valid():
            code_trick = form.save()
            code_trick.save()
            return HttpResponseRedirect('/')
        return render(request, 'tricks/new.html', {'form': form})