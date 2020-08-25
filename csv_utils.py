import os
import csv
import collections

data = []

Contact = collections.namedtuple(
    'Contact',
    'first_name,last_name'
)


# Load csv into memory
def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'import.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            contact = parse_row(row)
            data.append(contact)

        return data


def parse_row(row):
    row['first_name'] = str(row['first_name'])
    row['last_name'] = str(row['last_name'])

    record = Contact(
        **row
    )

    return record