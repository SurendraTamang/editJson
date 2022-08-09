from cgitb import reset
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request=request, template_name="tokenlist/index.html",context={
        "title":"Learning"
    })
    