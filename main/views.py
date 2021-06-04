from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def main_view(request):
    return render(request, 'main/main.html', {'name': 'Alexander'})


def main_view_api(request):
    return JsonResponse({'message': 'ok'})
