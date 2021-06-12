from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.utils import field_mapping
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie',)

        