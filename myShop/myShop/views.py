from django.http.request import HttpRequest
from django.http.response import HttpResponse


def main_page(request: HttpRequest):
    """mock func for path: '/"""
    return HttpResponse('<h1> main page </h1>')
    