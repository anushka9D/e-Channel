from django.shortcuts import render

# Create your views here.


def index(request):
    #return HttpResponse("Hello, world!")

    # Render the 'index.html' template located in 'templates/myapp/'
    return render(request, 'index.html')

def login_view(request):
    return render(request, '/login.html')