from rest_framework import serializers
from .models import Job, Candidate


class ApplyjobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['Name', 'Email', 'Phone', 'Position', 'CV']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['Id', 'Title', 'Job_Type',
                  'is_published', 'Open_date', 'Close_date']


class HasOpeningSerializer(serializers.Serializer):
    has_opening = serializers.BooleanField()
