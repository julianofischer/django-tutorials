from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Documento

# Create your views here.
class DocumentsListView(ListView):
    model = Documento
    template_name = 'documento_list.html'
