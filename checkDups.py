import csv

all_perth_file = open('all_perth.csv', 'r')
all_perth_reader = csv.reader(all_perth_file)

property_sales_file = open('Property_Sales.csv', 'r')
property_sales_reader = csv.reader(property_sales_file)

all_perth_addresses = set()
property_sales_addresses = set()

for row in all_perth_reader:
    all_perth_addresses.add(row[0])

for row in property_sales_reader:
    property_sales_addresses.add(row[0])

duplicates = all_perth_addresses.intersection(property_sales_addresses)

print(f'There are {len(duplicates)} duplicate Address values between all_perth.csv and Property_Sales.csv')


for duplicate in duplicates:
    print(duplicate)
