import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("Hello Django!")
    return render(
        request,
        "index.html",
        {
            "username": "admin",
            "password": "Django123456",
        },
    )
