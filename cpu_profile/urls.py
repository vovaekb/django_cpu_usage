from django.urls import path
from .views import records_list, records_table


urlpatterns = [
    path('api/records/', records_list),
    path('records', records_table)
]