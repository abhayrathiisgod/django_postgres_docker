from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Job, Candidate
from .serializers import JobSerializer, HasOpeningSerializer, ApplyjobSerializer
from rest_framework.response import Response
# Create your views here.


class JobView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Applyjob(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = ApplyjobSerializer


class JobViewSingle(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'pk'


class HasOpening(APIView):
    def get(self, request, *args, **kwargs):
        has_opening = Job.objects.exists()
        data = {'has_opening': has_opening}
        serializer = HasOpeningSerializer(data)
        return Response(serializer.data)
