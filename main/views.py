from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Main

# Create your views here.


def main_view(request):
    return render(request, 'main/main.html', {'name': 'Alexander'})


def main_view_api_echo(request):
    return JsonResponse({'message': 'ok'})


def main_view_api_questions(request):
    data = Main.objects.all()[0].settings
    return JsonResponse(
        {'data': data},
        headers={'content_type': 'application/json; charset=utf-8'},
    )
