from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from csv_web_app_server.file_upload.models import CsvUpload
from csv_web_app_server.file_upload.serializers import CsvUploadSerializer

from .utilities import convert_csv_to_json

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

    @detail_route(methods=['get'])
    def get_data(self, request, pk=None):
        document = self.get_object()
        print(document)
        filename = document.document
        print(filename)
 
        data = convert_csv_to_json(filename)
        print(data)

        return Response(data=data, status=200)
