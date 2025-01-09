from django.contrib import admin
from reservation_app.api.models.tables_model import Table
from reservation_app.api.models.reservation_model import Reservation
from reservation_app.api.models.clients_model import Client

# Register your models here.

admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Client)