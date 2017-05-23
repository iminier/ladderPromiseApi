# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PromiseModel
from .serializer import PromiseSerializer

@api_view(['GET', 'POST'])
def promise_list(request):
    '''
    List all and Create New
    '''
    if request.method == 'GET':
        promises = PromiseModel.objects.all()
        serializer = PromiseSerializer(promises, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PromiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def promise_detail(request, pk):
    '''
    Retrieve, update or delete
    '''
    try:
        promise = PromiseModel.objects.get(pk=pk)
    except PromiseModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PromiseSerializer(promise)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PromiseSerializer(promise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        promise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
