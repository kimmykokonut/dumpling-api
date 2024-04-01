from django.http import JsonResponse
from .models import Dumpling
from .serializers import DumplingSerializer

def dumpling_list(request):
  # name url from urls.py pattern
  #get all dumplings
  dumplings = Dumpling.objects.all()
  #serialize
  serializer = DumplingSerializer(dumplings, many=True)
  #return json, as list
  # return JsonResponse(serializer.data, safe=False)
  # to return as json object
  return JsonResponse({"dumplings": serializer.data}, safe=False)
