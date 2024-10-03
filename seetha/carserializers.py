from rest_framework import serializers
from .models import *

class CLBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=CLBasicDetail
        fields='__all__'


class CarLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarLoan
        fields = '__all__'
        
class CarLoanDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarLoanDocument
        fields = '__all__'

class CarApplicationVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarApplicationVerification
        fields = '__all__'
