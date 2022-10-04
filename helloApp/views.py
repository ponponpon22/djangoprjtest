from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'helloApp/index.html')

def second (request):
    return render(request,'helloApp/second.html')
