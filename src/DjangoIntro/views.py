from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome to this sample page.</h1>")