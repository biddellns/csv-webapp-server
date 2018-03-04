from rest_framework import serializers
from .models import CsvUpload

class CsvUploadSerializer(serializers.ModelSerializer):
    document = serializers.FileField(read_only=True)

    class Meta:
        model = CsvUpload
        fields = ('pk', 'document', 'upload_date')
