from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.


def catalog_home(request: HttpRequest):
    return HttpResponse(f'<h1> catalog home page </h1>')
