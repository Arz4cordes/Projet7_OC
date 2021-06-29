# solution optimisée, avec un algo glouton
# puis en programmation dynamique
from time import time
# Classe action
# init avec nom, cout et benefice
# statut achetee ou non (false par defaut)
# recipe: calculer le benefice de l action


class Stocks:
    """ actions we can bought
    :param: name (type: string), cost (type:float), benefit (type: float)
    """

    stocks_list = []

    def __init__(self, name, cost, benefit):
        self.name = name
        self.cost = cost
        self.benefit = benefit
        self.bought = False
        self.recipe = cost * (1 + benefit / 100)
        self.efficiency = self.recipe / self.cost
        return Stocks.stocks_list.append(self)


# Entrée des différentes actions et du budget total
total_budget = 500
stock1 = Stocks("Action-1", 20,	5)
stock2 = Stocks("Action-2",	30,	10)
stock3 = Stocks("Action-3",	50,	15)
stock4 = Stocks("Action-4",	70,	20)
stock5 = Stocks("Action-5",	60,	17)
stock6 = Stocks("Action-6",	80,	25)
stock7 = Stocks("Action-7",	22,	7)
stock8 = Stocks("Action-8",	26,	11)
stock9 = Stocks("Action-9",	48,	13)
stock10 = Stocks("Action-10", 34, 27)
stock11 = Stocks("Action-11", 42, 17)
stock12 = Stocks("Action-12", 110, 9)
stock13 = Stocks("Action-13", 38, 23)
stock14 = Stocks("Action-14", 14, 1)
stock15 = Stocks("Action-15", 18, 3)
stock16 = Stocks("Action-16", 8, 8)
stock17 = Stocks("Action-17", 4, 12)
stock18 = Stocks("Action-18", 10, 14)
stock19 = Stocks("Action-19", 24, 21)
stock20 = Stocks("Action-20", 114, 18)
# Affichage des différentes actions et du nombre total de combinaison
for stock in Stocks.stocks_list:
    stocks_display = stock.name + " coût" + str(stock.cost)
    stocks_display += " pourcentage benefice: " + str(stock.benefit)
    stocks_display += " recette: " + str(stock.recipe)
    print(stocks_display)
n = len(Stocks.stocks_list)
p = 2 ** n
print(f"il y a {n} actions dans la liste,")
print(f"et {p} combinaisons possibles avec budget illimité")
# Trier Stocks.stocks_list par efficacité (efficiency)
# initialiser la liste combinaison
# coût embarqué = 0
# benef total = 0
# Pour chaque action dans les actions triées:
#   si l'action vérifie coût + coût embaqué <= coût total:
#       ajouter l'action à la combinaison
#       ajouter le coût au coût embarqué
#       ajouter la recette au benef total
#       ajouter l'action à la liste combinaison
# Afficher la combinaison retenue, le coût total et le benef total
stocks_by_efficiency = sorted(Stocks.stocks_list, key=lambda stock: stock.efficiency)
for stock in stocks_by_efficiency:
    print(stock.name)
    