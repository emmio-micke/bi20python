import csv

with open('/Users/micke/www/projects/nackademin/BI20/python/bi20python/code/11 - csv/customers.csv', mode='r') as customers_file:
    csv_customers = csv.reader(customers_file, delimiter=';')
    line_count = 0
    headers = []
    new_customers_list = []

    for row in csv_customers:
        if line_count == 0:
            headers = row
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        if row[10] == 'USA' or row[10] == 'France':
            new_customers_list.append(row)

with open('/Users/micke/www/projects/nackademin/BI20/python/bi20python/code/11 - csv/customers_new.csv', mode='w') as new_customers_file:
    customers_writer = csv.writer(new_customers_file, delimiter=';')

    customers_writer.writerow(headers)

    for customer_row in new_customers_list:
        customers_writer.writerow(customer_row)
