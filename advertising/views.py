from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertising

# def my_view(request):
#     return HttpResponse("Hello, World!")

def my_view(request):
    return render(request, 'advertising/my_template.html')

def client_advertising_list(request,client_id):
    advertisings = Advertising.objects.filter(client_id=client_id)

    context = {
        'client_id': client_id,
        'advertisings': advertisings,
    }

    return render(request, 'advertising/client_advertising_list.html', context)

