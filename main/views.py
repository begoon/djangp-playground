from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Main

# Create your views here.


def main_view(request):
    return render(request, 'main/main.html', {'name': 'Alexander'})


def main_view_api_echo(request):
    return JsonResponse({'message': 'ok'})


@api_view(['GET'])
def main_view_api_questions(request):
    data = Main.objects.all()[0].settings
    return Response(data)
