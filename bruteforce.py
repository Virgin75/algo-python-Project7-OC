import csv
import time

start_time = time.time()

csv_shares = []
MONEY = 500

choosen_shares = []


class Share:
    def __init__(self, cost, rate, name):
        self.cost = int(cost)
        self.rate = int(rate[:-1])
        self.name = name
        self.return_on_investment = self.cost * (1 + self.rate / 100) - self.cost
        self.ratio = self.return_on_investment / self.cost

    def __str__(self):
        return f'{self.name} - ROI: {self.return_on_investment}, Price: {self.cost}, Ratio: {self.ratio}'


''' Read the csv file'''
with open('bruteforce-data.csv') as file:
    data = csv.DictReader(file, delimiter=',')
    for row in data:
        csv_shares.append(Share(row['cost'], row['rate'], row['name']))


'''Bruteforce'''


def roi_total(shares_list):
    value = 0
    for share in shares_list:
        value += share.return_on_investment
    return value


def money_spent(shares_list):
    value = 0
    for share in shares_list:
        value += share.cost
    return value


def force_brute(shares_list, money):
    nb_shares = len(shares_list)
    nb_possibilites = 2 ** nb_shares
    best_choice = []  # stocke la meilleure combianison

    for cle in range(nb_possibilites):
        chaine = bin(cle)[2:]  # ex: bin(67) prints 'Ob1000011' => bin(67)[2:] prints '1000011'
        long = len(chaine)  # ex: len(bin(67)) prints 7

        if long < nb_shares:  # On ajoute les 0 manquants de manière à ce que len(chaine) soit tjrs égale à 20
            chaine = (nb_shares - long) * '0' + chaine
        # print(chaine)
        combinaison = []
        for i in range(nb_shares):
            if chaine[i] == '1':
                combinaison.append(shares_list[i])
        if roi_total(combinaison) > roi_total(best_choice):
            if money_spent(combinaison) <= money:
                best_choice = combinaison
                global choosen_shares
                choosen_shares = combinaison


force_brute(csv_shares, MONEY)

print('You shoud buy the following shares:')
for itm in choosen_shares:
    print(f'     - {itm}')

print(f'TOTAL PROFIT: {roi_total(choosen_shares)}€')
print(f'MONEY SPENT: {money_spent(choosen_shares)}€')

print("--- %s seconds ---" % (time.time() - start_time))
