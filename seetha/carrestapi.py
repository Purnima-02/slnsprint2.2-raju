from .carserializers import *
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.decorators import action
from .models import *

class CarLoanViewSet(viewsets.ModelViewSet):
    queryset = CarLoan.objects.all()
    serializer_class = CarLoanSerializer
    
   
    def getByRefCode(self , refCode ):
        try:
            queryset = CarLoan.objects.filter(ref_code=refCode).prefetch_related('personal_detail')
            if queryset.exists():
                CarLoanSerializer = self.get_serializer(queryset, many=True)
                return Response(CarLoanSerializer.data, status=200)
            else:
                return Response({"message": "No Records Found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class CarLoanDocumentViewSet(viewsets.ModelViewSet):
    queryset = CarLoanDocument.objects.all()
    serializer_class = CarLoanDocumentSerializer
    
class CarApplicationVerifyViewSet(viewsets.ModelViewSet):
    queryset = CarApplicationVerification.objects.all()
    serializer_class = CarApplicationVerificationSerializer
    # permission_classes = [IsAuthenticated]
