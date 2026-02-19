from django.shortcuts import render

# Create your views here.
def contacts(request):
    return render(request,'contacts.html')
def gallery(request):
    return render(request,'gallery.html')
def index(request):
    return render(request,'index.html')
def tickets(request):
    return render(request,'tickets.html')
def about(request):
    return render(request,'about.html')
def schedule(request):
    return render(request,'schedule.html')

