import logging

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from csv_web_app_server.file_upload.models import CsvUpload
from csv_web_app_server.file_upload.serializers import CsvUploadSerializer

class CsvUploadViewSet(viewsets.ModelViewSet):
    queryset = CsvUpload.objects.all()
    serializer_class = CsvUploadSerializer

class CsvUploadApiView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request):
        try:
            file_obj = request.FILES['upload']
            serializer = CsvUploadSerializer(data={'document':file_obj})
            serializer.is_valid()

            return Response(data=serializer.data, status=201)
        except:
            return Response(status=400)
