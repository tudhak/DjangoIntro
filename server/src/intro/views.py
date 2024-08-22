from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "intro/index.html")

def topic(request, topic_num):
    if not topic_num in ["A", "B", "C"]:
        return render(request, "intro/topic_not_found.html")

    return render(request, f"intro/topic{topic_num}.html")
