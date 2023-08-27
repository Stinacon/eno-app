from django.core.management.base import BaseCommand
import csv
from eno.models import Craft


class Command(BaseCommand):
    help = 'Loads craft artists from csv into database'

    def handle(self, *args, **kwargs):
        with open('crafter_data.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(
                        f'\t{row[3]} is a {row[5]} artist.')
                    try:
                        new_crafter = Craft(
                            business_name=row[3],
                            contact_name=row[7] + row[8],
                            email=row[9],
                            phone=row[10],
                            address_street=row[11],
                            address_city=row[12],
                            address_state=row[13],
                            address_zip=row[14],
                            bio=row[16],
                            url=row[21],
                            booth_number=row[4])
                        new_crafter.save()
                        line_count += 1
                    except:
                        print('Error loading artist')
            print(f'Processed {line_count} lines.')
