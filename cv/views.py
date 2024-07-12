from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'languages.html')

def education_view(request):
    return render(request,'education.html')

def Abilities_view(request):
    return render(request,'Abilities.html')

def contact_view(request):
    return render(request,'contact.html')
