import csv
import json

def convert_csv_to_json(input_file):
    reader = csv.reader(input_file.read().decode('utf-8').splitlines())

    rows = []
    headers = []
    for index, row in enumerate(reader):
        if index == 0:
            headers = row
        else:
            data_row = {}
            for index, column in enumerate(row):
                data_row[headers[index]] = column
            rows.append(data_row)

    return rows
