from django.shortcuts import render

# Create your views here.
def index(request):
    name="Hello Satwik"
    return render(request,"myapp/index.html",{'name':name})