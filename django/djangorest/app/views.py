import io

from django.http import HttpResponse
from .models import AiQuest
from .serializers import AiQuestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#Queryset
def aiquest_info(request):
    #complex data
    ai= AiQuest.objects.all()
    #python dict
    serializer = AiQuestSerializer(ai, many=True)
    # render Json
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# @csrf_exempt
# def aiquest_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         #json to stream convert
#         stream = io.BytesIO(json_data)
#         #stream to python 
#         pythondata = JSONParser().parse(stream)
#         #python to complex data
#         serializer = AiQuestSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Successfully inserted data'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == 'PUT':
#         json_data = request.body
#         #json to stream convert
#         stream = io.BytesIO(json_data)
#         #stream to python 
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         ai = AiQuest.objects.get(id=id)
#         #python to complex data
#         serializer = AiQuestSerializer(ai, data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Successfully updated data'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     if request.method == 'DELETE':
#         json_data = request.body
#         #json to stream c onvert
#         stream = io.BytesIO(json_data)
#         #stream to python 
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         ai = AiQuest.objects.get(id=id)
#         ai.delete()
#         res = {'msg': 'Successfully deleted data'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
    

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def aiquest_create(request, pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None:
            #complex data
            ai = AiQuest.objects.get(id=id)
            #python dict
            serializer = AiQuestSerializer(ai)
            # render Json
            return Response(serializer.data)
        
        #complex data
        ai = AiQuest.objects.all()
        #python dict
        serializer = AiQuestSerializer(ai, many=True)
        # render Json
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AiQuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res= {'msg': 'Successfully inserted data'}
            return Response(res, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'PUT':
        id=pk
        ai = AiQuest.objects.get(id=id)
        serializer = AiQuestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res= {'msg': 'Successfully updated full data'}
            return Response(res)
        return Response(serializer.errors, status=400)


    if request.method == 'PATCH':
        id=pk
        ai = AiQuest.objects.get(id=id)
        serializer = AiQuestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res= {'msg': 'Successfully updated partial data'}
            return Response(res)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        id=pk
        ai = AiQuest.objects.get(id=id)
        ai.delete()
        res= {'msg': 'Successfully deleted data'}
        return Response(res, status=204)