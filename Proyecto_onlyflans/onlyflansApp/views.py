from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bienvenido a OnlyFlans</h1>
        <p>Los mejores flanes del mundo mundial</p>
    """)
# Create your views here.
