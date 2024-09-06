from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from dateutil.relativedelta import relativedelta
from datetime import date
from .models import *
from .serializers import SubscriberSerializer
from .utils import queryFrame

class SubscriberView(APIView):
    def get(self, request):
        data = Subscriber.objects.all()
        subscriberSerializer = SubscriberSerializer(data, many=True)
        return Response(subscriberSerializer.data)
    def post(self, request):
        subscriberserializer = SubscriberSerializer(data = request.data)
        if subscriberserializer.is_valid():
            try:
                subscriberserializer.save()
            except Exception as exc:
                print(exc)
                return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(subscriberserializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(subscriberserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubscriberViewById(APIView):
    def get(self, request, id):
        data = Subscriber.objects.get(pk=id)
        subscriberSerializer = SubscriberSerializer(data)
        return Response(subscriberSerializer.data)

@api_view(['GET'])
def getSubscribersByFilter(request):
    ageStart = request.GET.get('ageStart')
    ageEnd = request.GET.get('ageEnd')
    education = request.GET.get('education')
    gender = request.GET.get('gender')
    heightStart = request.GET.get('heightStart')
    heightEnd = request.GET.get('heightEnd')
    weightStart = request.GET.get('weightStart')
    weightEnd = request.GET.get('weightEnd')
    caste = request.GET.get('caste')
    salaryStart = request.GET.get('salaryStart')
    salaryEnd = request.GET.get('salaryEnd')
    filterSql='SELECT * FROM public."SubscriberManagement_subscriber"'
    arg = []
    index=0
    if ageStart is not None and ageEnd is not None:
        dateEnd = date.today() - relativedelta(years=int(ageStart)-1)
        dateStart = date.today() - relativedelta(years=int(ageEnd)+1)
        filterSql+=queryFrame(index, 'date_of_birth', None, 'BETWEEN')
        arg.append(dateStart)
        arg.append(dateEnd)
        index+=1
    if heightStart is not None and heightEnd is not None:
        filterSql+=queryFrame(index, 'height', None, 'BETWEEN')
        arg.append(heightStart)
        arg.append(heightEnd)
        index+=1
    if weightStart is not None and weightEnd is not None:
        filterSql+=queryFrame(index, 'weight', None, 'BETWEEN')
        arg.append(weightStart)
        arg.append(weightEnd)
        index+=1
    if salaryStart is not None and salaryEnd is not None:
        filterSql+=queryFrame(index, 'salary', None, 'BETWEEN')
        arg.append(salaryStart)
        arg.append(salaryEnd)
        index+=1
    if education is not None:
        filterSql+=queryFrame(index, 'education', None, 'LIKE')
        arg.append('%'+education+'%')
        index+=1
    if gender is not None:
        filterSql+=queryFrame(index, 'gender', None, '=')
        arg.append(gender)
        index+=1
    if caste is not None:
        filterSql+=queryFrame(index, 'caste', None, 'LIKE')
        arg.append('%'+caste+'%')
        index+=1
    try:
        data = Subscriber.objects.raw(filterSql, arg)
        subscriberSerializer = SubscriberSerializer(data, many=True)
        return Response(subscriberSerializer.data)
    except Exception as exc:
        print(exc)
        return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
