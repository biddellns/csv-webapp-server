import csv
from django.core.exceptions import ValidationError

def import_csv_file_validator(input_file):
    try:
        dialect = csv.Sniffer().sniff(input_file.read(1024).decode('utf-8'))
        input_file.seek(0)
    except csv.Error:
        raise ValidationError('Not a valid CSV file')
