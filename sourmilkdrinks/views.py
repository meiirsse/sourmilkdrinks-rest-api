from django.http import JsonResponse
from .models import SourMilkDrinks
from .serializers import SourMilkDrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def sourmilkdrink_list(request, format=None):
    
    if request.method == 'GET':
        sourmilkdrinks = SourMilkDrinks.objects.all()
        serializer = SourMilkDrinkSerializer(sourmilkdrinks, many=True)
        return JsonResponse({'sour milk drinks': serializer.data})
    
    if request.method == 'POST':
        serializer = SourMilkDrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def sourmilkdrink_detail(request, id, format=None):
    
    try:
        sourmilkdrink = SourMilkDrinks.objects.get(pk=id)
    except SourMilkDrinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SourMilkDrinkSerializer(sourmilkdrink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SourMilkDrinkSerializer(sourmilkdrink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sourmilkdrink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    