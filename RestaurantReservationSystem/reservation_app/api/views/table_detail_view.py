from rest_framework.views import APIView
from reservation_app.api.models.tables_model import Table
from reservation_app.api.serializers.tables_serializer import TableSerializer
from rest_framework.response import Response
from rest_framework import status

class TableDetailView(APIView):

    def get(self, request, pk):
        try:
            client = Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TableSerializer(client, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            client = Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TableSerializer(client, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            client = Table.objects.get(pk=pk)
            client.delete()
            return Response({'Response':'Table deleted'},status=status.HTTP_204_NO_CONTENT)
        except Table.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
