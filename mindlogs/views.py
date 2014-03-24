from django.views import generic
from models import IndexModel

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = IndexModel