import csv

with open('/Users/micke/www/projects/nackademin/BI20/python/bi20python/code/11 - csv/employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['name', 'department', 'birthday month'])
    employee_writer.writerow(['Kalle', 'Marketing', 'August'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
