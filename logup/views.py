from django.http import HttpResponse
from .models import info
from django.views import generic

'''def index(request):
    return HttpResponse("you are at my login page")'''

class IndexView(generic.ListView):
    model = info
    template_name = '/logup/index.html'
