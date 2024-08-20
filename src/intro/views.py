from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Introduction section of the website</h1>")