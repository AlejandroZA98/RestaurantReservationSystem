from reservation_app.api.models.clients_model import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='client-detail')

    class Meta:
        model=Client
        fields='__all__'
        