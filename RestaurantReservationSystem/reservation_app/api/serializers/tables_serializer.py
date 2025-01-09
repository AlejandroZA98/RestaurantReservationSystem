from reservation_app.api.models.tables_model import Table
from rest_framework import serializers
from django.contrib.auth.models import User

class TableSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='table-detail')
    class Meta:
        model=Table
        fields='__all__'
      