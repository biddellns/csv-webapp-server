from rest_framework import serializers
from .models import CsvUpload

class CsvUploadSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    document = serializers.FileField(required=False)
=======
    document = serializers.FileField()
>>>>>>> develop

    class Meta:
        model = CsvUpload
        fields = ('pk', 'document', 'upload_date')
