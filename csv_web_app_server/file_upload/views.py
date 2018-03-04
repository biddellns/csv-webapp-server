import logging

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response

from csv_web_app_server.file_upload.models import CsvUpload
from csv_web_app_server.file_upload.serializers import CsvUploadSerializer

class CsvUploadViewSet(viewsets.ModelViewSet):
    queryset = CsvUpload.objects.all()
    serializer_class = CsvUploadSerializer

    def perform_create(self, serializer):
        serializer.save(document=self.request.data)

class CsvUploadApiView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request):
        file_obj = request.FILES['upload']

            #with open(filename, 'wb') as f:
            #   for chunk in f.chunks():
            #        f.write(chunk)
        serializer = CsvUploadSerializer(data=request.data)
        print(serializer.is_valid())
        serializer.is_valid()
        serializer.save()
        return Response(data=request.FILES, status=201)
#        except:
#            return Response(data=request.FILES, status=400)
