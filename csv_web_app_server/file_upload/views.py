from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from csv_web_app_server.file_upload.models import CsvUpload
from csv_web_app_server.file_upload.serializers import CsvUploadSerializer

class CsvUploadViewSet(viewsets.ModelViewSet):
    queryset = CsvUpload.objects.all()
    serializer_class = CsvUploadSerializer
    parser_classes = (MultiPartParser,)

    def create(self, request):
        try:
            file_obj = request.FILES['upload']
            serializer = CsvUploadSerializer(data={'document':file_obj})
            serializer.is_valid()
            serializer.save()

            return Response(serializer.data, status=HTTP_201_CREATED)
        except:
            return Response(status=HTTP_400_BAD_REQUEST)


