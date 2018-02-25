import csv
from ast import literal_eval

from django.core.exceptions import ValidationError

def import_csv_file_validator(input_file):
    try:
        stream = input_file.read().decode('utf-8')
        hasHeaders = csv.Sniffer().has_header(stream)
        dialect = csv.Sniffer().sniff(stream)
        print('did we get here')
        input_file.seek(0)
    except csv.Error:
        raise ValidationError('Not a valid CSV file')

    reader = csv.reader(input_file.read().decode('utf-8').splitlines(), dialect)

    for row, column in enumerate(reader):
        # Header check is in a different validator
        if row > 0:
            for index, value in enumerate(column):

                # Don't validate the first column
                if index > 0:
                    if not is_valid_column_data(value):
                        errMsg = 'Not valid column data: {} | row, column: {}, {}'.format(value,
                                row, index + 1)
                        raise ValidationError(errMsg)

def is_valid_column_data(value):
    value = literal_eval(value)

    is_float_or_int = (isinstance(value, int) or isinstance(value, float))

    return is_float_or_int and value >= 0
