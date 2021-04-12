'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: CSV (Write CSV)
'''
import csv


with open('employee.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Suraj', 'DBA', 'November'])
    employee_writer.writerow(['Sharad', 'IT', 'March'])
