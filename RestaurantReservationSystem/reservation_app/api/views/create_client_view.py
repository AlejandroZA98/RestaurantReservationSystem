from reservation_app.api.models.clients_model import Client
from reservation_app.api.serializers.clients_serializer import ClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateClientView(APIView):
    def post(self,request):
        serializer = ClientSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)