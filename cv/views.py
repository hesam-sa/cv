from django.shortcuts import render

# Create your views here.
context = {'name':'Hesam Sadat',"address":"no.44,ahmadabad str,mashhad,iran",'phone':'09151105001','email':'hesam.sadat@gmail.com'}
def index_view(request):
    return render(request,'index.html',context)

def about_view(request):
    return render(request,'languages.html')

def education_view(request):
    return render(request,'education.html')

def Abilities_view(request):
    return render(request,'Abilities.html')

def contact_view(request):
    return render(request,'contact.html',context)
