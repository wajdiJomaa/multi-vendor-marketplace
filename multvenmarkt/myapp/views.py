from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def wajdi(request):
    return render(request, "index.html")
def home():
    print("hello")
