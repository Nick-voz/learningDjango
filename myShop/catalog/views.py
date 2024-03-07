from django.http.request import HttpRequest
from django.http.response import HttpResponse


def catalog_home(request: HttpRequest):
    """mock func for path: './catalog/"""
    return HttpResponse('<h1> catalog home page </h1>')
