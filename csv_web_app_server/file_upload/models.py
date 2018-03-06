from django.db import models

from .validators import import_csv_file_validator

# Create your models here.
class CsvUpload(models.Model):
    document = models.FileField(upload_to="media", validators=[import_csv_file_validator])
    upload_date = models.DateField(auto_now=True)
