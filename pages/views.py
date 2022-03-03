from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'pages/about.html')

def partners(request):
    return render(request, 'pages/partners.html')

def contact(request):
    return render(request, 'pages/contact.html')