import csv
import time

start_time = time.time()
benefices = []

with open('bruteforce-data.csv') as file:
    data = csv.DictReader(file, delimiter=',')
    for row in data:
        benefices.append({'name': row['name'], 'ROI': int(row['cost']) *
                          (1 + int(row['benef'][:-1]) / 100) - int(row['cost'])})

sorted_benef = sorted(benefices,  key=lambda item: item['ROI'], reverse=True)
print(sorted_benef)
print("--- %s seconds ---" % (time.time() - start_time))
