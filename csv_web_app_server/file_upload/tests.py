from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.datetime_safe import datetime

from csv_web_app_server.file_upload.models import CsvUpload

@override_settings(MEDIA_ROOT='/tmp/django')
class CsvUploadModelTest(TestCase):

    def setUp(self):
        my_file = SimpleUploadedFile('file.csv', b'1,2,3,4,5,6')

        self.csv_upload = CsvUpload()
        self.csv_upload.document = my_file

        self.date = datetime.now().date()
        self.csv_upload.save()

    def test_model_after_save(self):
        document = self.csv_upload.document

        text = document.read()
        csv_upload_date = self.csv_upload.upload_date

        self.assertEquals(b'1,2,3,4,5,6', text)
        self.assertEquals(self.date, csv_upload_date)
