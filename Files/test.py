import csv

filepath = input(" please input filepath of csv file : ")
with open(filepath, 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)