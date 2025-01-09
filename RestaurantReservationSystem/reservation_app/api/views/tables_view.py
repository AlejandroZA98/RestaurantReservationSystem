from rest_framework import mixins, generics
from reservation_app.api.models.tables_model import Table
from reservation_app.api.serializers.tables_serializer import TableSerializer
from rest_framework import filters

class TablesView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['name']
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)