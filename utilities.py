import csv

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
            line_count += 1
    print(f'Processed {line_count} lines.')