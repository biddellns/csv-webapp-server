import csv
import json

def convert_csv_to_json(input_file):
    #    stream = input_file.read().decode('utf-8')
    #dialect = csv.Sniffer().sniff(stream)

    #reader = csv.reader(stream.splitlines())
    reader = csv.reader(input_file.read().decode('utf-8').splitlines())

    rows = []
    for row, column in enumerate(reader):
        new_row = {}
        for index, value in enumerate(column):
            new_row[index] = value
        rows.append(new_row)

    
    print(json.dumps(rows))
    return json.dumps(rows)
