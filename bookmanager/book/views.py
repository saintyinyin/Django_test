from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('ok')
    context = {
        'name' : 'Show me the money!'
    }
    return render(request, "book/index.html", context = context)