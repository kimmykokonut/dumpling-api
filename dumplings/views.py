from django.http import JsonResponse
from .models import Dumpling, Tag, Origin
from .serializers import DumplingSerializer, TagSerializer, OriginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

@api_view(['GET', 'POST'])
def dumpling_list(request, format=None):
  # GET /dumplings
  if request.method == 'GET':
    # name url from urls.py pattern
    # get all dumplings
    dumplings = Dumpling.objects.all()
    # call paginator in view
    paginator = PageNumberPagination()
    paginator.page_size = 20
    #apply pagination
    paginated_dumplings = paginator.paginate_queryset(dumplings, request)
    # serialize data
    serializer = DumplingSerializer(paginated_dumplings, many=True)
    ##return json, as list
    # return JsonResponse(serializer.data, safe=False)
    ## to return as json object
    # return JsonResponse({"dumplings": serializer.data})
    ## !to return-BestPractice-using RestFramework Response
    #return Response(serializer.data)
    #return paginated data
    return paginator.get_paginated_response(serializer.data)
  if request.method == 'POST':
    # add a dumpling
    serializer = DumplingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  
# dumplings/1
@api_view(['GET', 'PUT', 'DELETE'])  
def dumpling_detail(request, id,):
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

#tags/
@api_view(['GET', 'POST'])
def tag_list(request, format=None):
  if request.method == 'GET':
    tags = Tag.objects.all() 
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

#tags/1
@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail(request, pk):
  try:
    tag = Tag.objects.get(pk=pk)
  except Tag.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = TagSerializer(tag)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = TagSerializer(tag, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
# /origins
@api_view(['GET', 'POST'])
def origin_list(request, format=None):
  if request.method == 'GET':
    origins = Origin.objects.all()
    serializer = OriginSerializer(origins, many=True)
    return Response(serializer.data)
  if request.method == 'POST':
    serializer = OriginSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# /origins/1
@api_view(['GET', 'PUT', 'DELETE'])
def origin_detail(request, pk):
  try:
    origin = Origin.objects.get(pk=pk)
  except Origin.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = OriginSerializer(origin)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = OriginSerializer(origin, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    origin.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)