import csv
import time

start_time = time.time()

shares = []
choosen_shares = []
total_roi = 0
MONEY = 500


class Share:
    def __init__(self, cost, rate, name):
        self.cost = int(cost)
        self.rate = int(rate[:-1])
        self.name = name
        self.return_on_investment = self.cost * (1 + self.rate / 100) - self.cost
        self.ratio = self.return_on_investment / self.cost

    def __str__(self):
        return f'{self.name} - ROI: {self.return_on_investment}, Price: {self.cost}, Ratio: {self.ratio}'


'''Algo Glouton sac à dos'''

with open('bruteforce-data.csv') as file:
    data = csv.DictReader(file, delimiter=',')
    for row in data:
        shares.append(Share(row['cost'], row['rate'], row['name']))

sorted_benef = sorted(shares,  key=lambda share: share.ratio, reverse=True)
for share in sorted_benef:
    if MONEY >= share.cost:
        choosen_shares.append(share)
        MONEY -= share.cost


for itm in choosen_shares:
    total_roi += itm.return_on_investment
    print(itm)

print(total_roi)

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
    reponse = []

    for cle in range(nb_possibilites):  # il y a nombre possibilités de 0 à 127
        chaine = bin(cle)[2:]
        long = len(chaine)
        if long < nb_shares:
            chaine = (nb_shares - long) * '0' + chaine
        # print(chaine)
        combinaison = []
        for i in range(nb_shares):
            if chaine[i] == '1':
                combinaison.append(shares_list[i])
        if roi_total(combinaison) > roi_total(reponse):
            if money_spent(combinaison) < money:
                reponse = combinaison
                print("Trouvé mieux :")
                for itm in reponse:
                    print(itm)
                print("Ce qui fait", roi_total(reponse), "€ de ROI")
                print("pour", money_spent(combinaison), "€ dépensés.")


force_brute(shares, MONEY)

print("--- %s seconds ---" % (time.time() - start_time))
