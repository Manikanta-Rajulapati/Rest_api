from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
def test_view(request):
    data = {
        'name': 'John',
        'age': 23
    }
    return JsonResponse(data)