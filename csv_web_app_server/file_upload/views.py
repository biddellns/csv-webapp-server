import logging

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from csv_web_app_server.file_upload.models import CsvUpload
from csv_web_app_server.file_upload.serializers import CsvUploadSerializer

class CsvUploadViewSet(viewsets.ModelViewSet):
    queryset = CsvUpload.objects.all()
    serializer_class = CsvUploadSerializer

    def perform_create(self, serializer):
        serializer.save(document=self.request.data)

class CsvUploadApiView(APIView):
    logger = logging.getLogger(__name__)

    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, filename):
        try:
            logger.info('Received ' + filename)
            file_obj = request.data['file']

            #with open(filename, 'wb') as f:
            #   for chunk in f.chunks():
            #        f.write(chunk)

            CsvUploadSerializer(document=file_obj)
            return Response(status=201)
        except:
            return Response(status=400)
