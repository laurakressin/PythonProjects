import csv

csvfile = open('../data-wrangling-master/data/chp3/data-text.csv', 'rb')
reader = csv.DictReader(csvfile)

for row in reader:
    print row