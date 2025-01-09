from reservation_app.api.models.tables_model import Table
from reservation_app.api.serializers.tables_serializer import TableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateTableView(APIView):
    def post(self,request,pk):
        data=request.data
        print("LA DATA",data)
        data['user']=pk
        serializer = TableSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)