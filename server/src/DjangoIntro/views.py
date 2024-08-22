from datetime import datetime

from django.shortcuts import render


def index(request):
    date = datetime.today()
    return render(request, "DjangoIntro/index.html", context={"username": "anonymous_user", "date": date})