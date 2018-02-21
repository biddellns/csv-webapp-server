from django.db import models

from .validators import import_csv_file_validator

# Create your models here.
class Csv_Upload(models.Model):
    document = models.FileField(validators=[import_csv_file_validator])
    upload_date = models.DateField(auto_now=True)
