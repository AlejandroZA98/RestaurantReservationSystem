from django.contrib import admin
from django.urls import path,include
from reservation_app.api.views.create_table_view import CreateTableView
from reservation_app.api.views.tables_view import TablesView
from reservation_app.api.views.table_detail_view import TableDetailView
from reservation_app.api.views.create_client_view import CreateClientView
from reservation_app.api.views.clients_view import ClientsView
from reservation_app.api.views.client_detail_view import ClientDetailView
from reservation_app.api.views.create_reservation_view import CreateReservationView

urlpatterns =[
    path('<int:pk>/create-table/',CreateTableView.as_view(),name='create-table'),
    path('tables/',TablesView.as_view(),name='tables'),
    path('table-detail/<int:pk>/',TableDetailView.as_view(),name='table-detail'),
    path('create-client/',CreateClientView.as_view(),name='create-client'),
    path('clients/',ClientsView.as_view(),name='clients'),
    path('client-detail/<int:pk>/',ClientDetailView.as_view(),name='client-detail'),
    path('create-reservation/',CreateReservationView.as_view(),name='create-reservation'),

]
