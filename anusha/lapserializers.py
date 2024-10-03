from rest_framework import serializers
from .models import *


class BasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=basicdetailform
        fields='__all__'



class LapDocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = lapDocumentUpload
        fields = '__all__'

class DisbursementDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = disbursementdetails
        fields = '__all__'


class LapApplicationVerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = lapApplicationVerification
        fields = '__all__'



class LoanApplicationSerializer(serializers.ModelSerializer):
    basic_detail = BasicDetailSerializer()
    lapdocument = LapDocumentUploadSerializer()
    applicationverification = LapApplicationVerificationSerializer()
    disbursementdetail=DisbursementDetailsSerializer()
    class Meta:
        model = LoanApplication
        fields = '__all__'




class goldbasicdetailSerializer(serializers.ModelSerializer):               
    class Meta:
        model=goldbasicdetailform
        fields='__all__'

class goldapplicationSerializer(serializers.ModelSerializer):
    goldbasicdetail=goldbasicdetailSerializer()
    class Meta:
        model=Goldloanapplication
        fields='__all__'

class otherbasicdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=otherbasicdetailform
        fields='__all__'

class otherloanSerializer(serializers.ModelSerializer):
    otherbasicdetail=otherbasicdetailSerializer()
    class Meta:
        model=otherloans
        fields='__all__'


