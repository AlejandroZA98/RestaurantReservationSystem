from reservation_app.api.models.reservation_model import Reservation
from reservation_app.api.serializers.reservation_serializer import ReservationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateReservationView(APIView):
    def post(self,request):
       
        serializer = ReservationSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)