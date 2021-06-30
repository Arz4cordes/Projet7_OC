# solution force brute avec parcours de toutes les combinaisons
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
        return Stocks.stocks_list.append(self)


class Combinations:

    combinations_list = []

    def __init__(self, an_id, a_list):
        self.id = an_id
        self.elements = a_list
        self.total_cost = 0
        self.total_recipe = 0
        self.gain = 0
        self.best_choice = False
        return Combinations.combinations_list.append(self)

    def display(self):
        text = "\n Combinaison: "
        for element in self.elements:
            text += " " + element
        text += "\n Coût total: " + str(self.total_cost)
        text += "\n Recette: " + str(self.total_recipe)
        the_profit = self.total_recipe - self.total_cost
        text += "\n Benefice total: " + str(the_profit)
        return print(text)


# test: afficher toutes les combinaisons, budget illimité
# print("\n AFFICHAGE DE TOUTES LES COMBINAISONS \n")
# for combination in Combinations.combinations_list:
#    combination.display()

# print("\n AFFICHAGE DE TOUTES LES OFFRES AVEC 100 EUROS DE BUDGET \n")
# for combination in Combinations.combinations_list:
#    if combination.total_cost <= total_budget:
#        combination.display()
#        print("GAIN: " + str(combination.gain))
#        if combination.gain == best_offer:
#            print("MEILLEURE OFFRE !")


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
# boucle i allant de 1 à p
#   initier les combinaisons avec le numéro i
starting_time = time()
for i in range(p):
    combination = Combinations(i, [])
# Création de toutes les combianaisons possibles:
# c = 0 (numéro de la combinaison)
# Boucle i allant de 1 à n (on place A1, puis A2, puis A3...)
#   Boucle j allant de 1 à 2**i:
#   on place des A1 puis des nonA1 puis des A1 puis des nonA1...
#       si j impair, l'element vaut Ai et on prend son cout,
#       sinon il vaut nonAi et le cout vaut 0
#       boucle k allant de 1 à 2 ** (N-i)
#           ajouter l'élément à la combinaison numero c
#           ajouter
#           c += 1
for i in range(n):
    c = 0
    for j in range(2 ** i):
        if j % 2 == 0:
            element = "nonA" + str(i+1)
            the_cost = 0
            the_recipe = 0
        else:
            element = "A" + str(i+1)
            the_cost = Stocks.stocks_list[i].cost
            the_recipe = Stocks.stocks_list[i].recipe
        for k in range(2 ** (n - i)):
            Combinations.combinations_list[c].elements.append(element)
            Combinations.combinations_list[c].total_cost += the_cost
            Combinations.combinations_list[c].total_recipe += the_recipe
            c += 1
# Calcul du gain et de la meilleure offre
best_offer = 0
a = 0
i = 0
for combination in Combinations.combinations_list:
    combination.gain = combination.total_recipe - combination.total_cost
    cond1 = combination.gain >= best_offer
    cond2 = combination.total_cost <= total_budget
    if cond1 and cond2:
        best_offer = combination.gain
        a = i
    i += 1
ending_time = time()
delay = ending_time - starting_time
print("\n Nombre total de combinaisons: ")
print(len(Combinations.combinations_list))
print("\n Meilleur offre: ")
Combinations.combinations_list[a].display()
print("\n Temps écoulé pour calculer la meilleure offre:")
print(delay)
