import os
import csv
import collections
from classes import Contact

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

def export_contacts(contacts):
    # TODO create a versioning system for backups with users create the number os backups to save

    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'export.csv')

    with open(filename, 'w', newline='') as csvexport:
        header = ['first_name', 'last_name']
        writer = csv.writer(csvexport)

        writer.writerow(header)

        for contact in contacts:
            writer.writerow([contact.first_name, contact.last_name])
