from rest_framework import viewsets

from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser

from csv_web_app_server.file_upload.models import CsvUpload
from csv_web_app_server.file_upload.serializers import CsvUploadSerializer

class CsvUploadViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FileUploadParser, FormParser)

    queryset = CsvUpload.objects.all()
    serializer_class = CsvUploadSerializer
