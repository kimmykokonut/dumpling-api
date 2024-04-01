from django.http import JsonResponse
from .models import Dumpling
from .serializers import DumplingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def dumpling_list(request, format=None):
  # GET /dumplings
  if request.method == 'GET':
    # name url from urls.py pattern
    # get all dumplings
    dumplings = Dumpling.objects.all()
    # serialize data
    serializer = DumplingSerializer(dumplings, many=True)
    ##return json, as list
    # return JsonResponse(serializer.data, safe=False)
    ## to return as json object
    # return JsonResponse({"dumplings": serializer.data})
    ## !to return-BestPractice-using RestFramework Response
    return Response(serializer.data)
  
  if request.method == 'POST':
    # add a dumpling
    serializer = DumplingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  
# dumplings/1
@api_view(['GET', 'PUT', 'DELETE'])  
def dumpling_detail(request, id, format=None):
  #make sure valid request
  try: 
    dumpling = Dumpling.objects.get(pk=id)
  except Dumpling.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = DumplingSerializer(dumpling)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = DumplingSerializer(dumpling, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    dumpling.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


