
import csv
import time

start_time = time.time()

csv_shares = []
MONEY = 500

choosen_shares = []
total_roi = 0
total_spent = 0


class Share:

    '''
    Model of a Share object. Use it to instanciate a share.
    '''

    def __init__(self, cost, rate, name):
        self.cost = float(cost)
        self.rate = float(rate)
        self.name = name
        self.return_on_investment = self.cost * (1 + self.rate / 100) - self.cost
        try:
            self.ratio = self.return_on_investment / self.cost
        except ZeroDivisionError:
            self.ratio = 0.0

    def __str__(self):
        return f'{self.name} - ROI: {self.return_on_investment}, Price: {self.cost}, Ratio: {self.ratio}'


# Read the csv file and load data into 'csv_shares' Python list
with open('dataset1.csv') as file:
    data = csv.DictReader(file, delimiter=',')
    # Time complexity: O(n)
    for row in data:
        if float(row['price']) > 0:
            csv_shares.append(Share(row['price'], row['profit'], row['name']))
    # > Tri des actions par ratio (celles qui ont le meilleur ratio sont les plus intéressantes à acheter)
    # Time complexity: O(n log n)
    csv_shares.sort(key=lambda share: share.ratio, reverse=True)


# Algo optimisé
# > Iteration sur chaque action : on achete celles qui ont le meilleur ratio jusqu'à épuisement des 500€
# Time complexity: O(n)
for share in csv_shares:
    if MONEY >= share.cost:
        choosen_shares.append(share)
        MONEY -= share.cost


# Display the final results
print('You shoud buy the following shares:')
for itm in choosen_shares:
    total_roi += itm.return_on_investment
    total_spent += itm.cost
    print(f'     - {itm}')

print(f'TOTAL PROFIT: {total_roi}€')
print(f'TOTAL SPENT: {total_spent}€')

print("--- %s seconds ---" % (time.time() - start_time))
