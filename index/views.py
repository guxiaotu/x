from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")
