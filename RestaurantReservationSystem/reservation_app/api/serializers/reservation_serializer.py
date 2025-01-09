from rest_framework import serializers
from reservation_app.api.models.reservation_model import Reservation
from reservation_app.api.models.clients_model import Client
from reservation_app.api.models.tables_model import Table

class ReservationSerializer(serializers.ModelSerializer):
    client=serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(),many=False)
    client_name = serializers.StringRelatedField(source='client', read_only=True)
    table=serializers.PrimaryKeyRelatedField(queryset=Table.objects.all(),many=False)
    class Meta:
        model=Reservation
        fields='__all__'
