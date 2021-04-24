import csv
import time

start_time = time.time()

csv_shares = []
MONEY = 500

choosen_shares = []


class Share:

    '''
    Model of a Share object. Use it to instanciate a share.
    '''

    def __init__(self, cost: float, rate: float, name: str):
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
with open('bruteforce-data.csv') as file:
    data = csv.DictReader(file, delimiter=',')
    for row in data:
        csv_shares.append(Share(row['price'], row['profit'], row['name']))


def roi_total(shares_list: list):
    '''
    Return the total ROI (€) of shares given a list of Share objects.
    '''

    value = 0
    for share in shares_list:
        value += share.return_on_investment
    return value


def money_spent(shares_list: list):
    '''
    Return the total cost (€) of shares given a list of Share objects.
    '''

    value = 0
    for share in shares_list:
        value += share.cost
    return value


def force_brute(shares_list: list, money: int):
    '''
    Allows you to find a list of the most profitable shares to buy given a specific amount
    of money to spend. The function returns nothing but when execution is done, the global
    variable 'choosen_shares' is updated.

    Parameters
    ----------
    :param list shares_list: the list containing all the Share objects to analyse.
    :param int money: the maximum money that can be spent in shares.
    '''

    nb_shares = len(shares_list)
    nb_possibilites = 2 ** nb_shares
    best_choice = []  # stocke la meilleure combianison temporaire

    for possibilite in range(nb_possibilites):
        binary = bin(possibilite)[2:]  # ex: bin(67) prints 'Ob1000011' => bin(67)[2:] prints '1000011'

        if len(binary) < nb_shares:  # On ajoute les 0 manquants de manière à ce que len(binary) soit tjrs = à len(nb_shares)
            binary = (nb_shares - len(binary)) * '0' + binary

        combinaison = []

        for i in range(nb_shares):
            if binary[i] == '1':
                combinaison.append(shares_list[i])

        if roi_total(combinaison) > roi_total(best_choice):
            if money_spent(combinaison) <= money:
                best_choice = combinaison
                global choosen_shares
                choosen_shares = combinaison
                #print(f'best solution found: {roi_total(combinaison)}€')


force_brute(csv_shares, MONEY)

# Display the final results
print('You shoud buy the following shares:')
for itm in choosen_shares:
    print(f'     - {itm}')

print(f'TOTAL PROFIT: {roi_total(choosen_shares)}€')
print(f'MONEY SPENT: {money_spent(choosen_shares)}€')

print("--- %s seconds ---" % (time.time() - start_time))
