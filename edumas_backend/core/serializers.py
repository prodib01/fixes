from rest_framework import serializers
from .models import School, Campus

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']        