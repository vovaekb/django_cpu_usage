from django.shortcuts import render
# from rest_framework import generics
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Max, Min, Avg
from .models import Records
from .serializers import RecordsSerializer


# class ListRecordsView(generics.ListAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = Records.objects.all()
#     serializer_class = RecordsSerializer

@api_view(['GET', 'POST'])
def records_list(request):
    # GET list of records, POST a new record
    if request.method == 'GET':
        records = Records.objects.all()
        records_serializer = RecordsSerializer(records, many=True)
        return JsonResponse(records_serializer.data, safe=False)
    elif request.method == 'POST':
        record_data = JSONParser().parse(request)
        records_serializer = RecordsSerializer(data=record_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse(records_serializer.data, status=status.HTTP_201_CREATED)
        print(records_serializer.errors)
        return JsonResponse(records_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def records_table(request):
    if request.method == 'GET':
        last_records = Records.objects.order_by('-date_time')[:100]
        max_last_record = last_records.aggregate(Max('value'))
        min_last_record = last_records.aggregate(Min('value'))
        avg_last_record = last_records.aggregate(Avg('value'))

        context = {
            'last_records': last_records,
            'max_last_record': max_last_record,
            'min_last_record': min_last_record,
            'avg_last_record': avg_last_record
        }
        return render(request, 'records_index.html', context)