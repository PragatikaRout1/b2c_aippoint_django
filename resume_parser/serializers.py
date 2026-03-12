from rest_framework_mongoengine import serializers
from .models import ResumeCollection

class ResumeCollectionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ResumeCollection
        fields = '__all__'
