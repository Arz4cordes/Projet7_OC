# solution force brute avec parcours de toutes les combinaisons
from time import time
import math
import matplotlib.pyplot as plt
# Classe action
# init avec nom, cout et benefice
# statut achetee ou non (false par defaut)
# recipe: calculer le benefice de l action


class Stocks:
    """ initialize a list of stocks
    :param: the type of name is a string
            stocks_list is a list of stocks
    """
    def __init__(self, name):
        self.name = name
        self.stocks_list = []

    def create_stock(self, name, cost, benefit):
        """ create an object of the class Stock, with name, cost, benefit """
        a_stock = Stock(name, cost, benefit)
        self.stocks_list.append(a_stock)

    def display(self):
        # Affichage des différentes actions et du nombre total de combinaison
        for stock in self.stocks_list:
            stocks_display = stock.name + " coût" + str(stock.cost)
            stocks_display += " pourcentage benefice: " + str(stock.benefit)
            stocks_display += " recette: " + str(stock.recipe)
            stocks_display += "\n efficacité: " + str(stock.efficiency)
            print(stocks_display)
        n = len(self.stocks_list)
        p = 2 ** n
        print(f"il y a {n} actions dans la liste,")
        print(f"et {p} combinaisons possibles avec budget illimité")


class Stock:
    """ actions we can bought
    :param: name (type: string), cost (type:float), benefit (type: float)
    """

    def __init__(self, name, cost, benefit):
        self.name = name
        self.cost = cost
        self.benefit = benefit
        self.bought = False
        self.recipe = math.floor(1000 * cost * (1 + benefit / 100)) / 1000
        self.efficiency = self.recipe / self.cost


class Combinations:
    """ initialize a list of combinations
    :param: combinations_list is a list of combinations
    """
    def __init__(self, num_of_stocks):
        p = 2 ** num_of_stocks
        self.num_of_combinations = p
        self.combinations_list = []

    def create_combination(self, an_id):
        """ create an object of the class Stock, with name, cost, benefit """
        a_combination = Combination(an_id)
        self.combinations_list.append(a_combination)


class Combination:

    def __init__(self, an_id):
        self.id = an_id
        self.elements = []
        self.total_cost = 0
        self.total_recipe = 0
        self.gain = 0
        self.best_choice = False

    def display(self):
        text = "\n Combinaison: "
        for element in self.elements:
            text += " " + element
        text += "\n Coût total: " + str(self.total_cost)
        text += "\n Recette: " + str(self.total_recipe)
        the_profit = math.floor(1000 * (self.total_recipe - self.total_cost))
        the_profit = the_profit / 1000
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
# Entrée des différentes actions
def five_stocks():
    list_of_five_stocks = Stocks("Liste de 5 actions")
    list_of_five_stocks.create_stock("Action-1", 12, 25)
    list_of_five_stocks.create_stock("Action-2", 2,	150)
    list_of_five_stocks.create_stock("Action-3", 1,	200)
    list_of_five_stocks.create_stock("Action-4", 2,	100)
    list_of_five_stocks.create_stock("Action-5", 4,	150)
    return list_of_five_stocks


def twenty_stocks():
    list_twenty_stocks = Stocks("Liste de 20 actions")
    list_twenty_stocks.create_stock("Action-1", 20,	5)
    list_twenty_stocks.create_stock("Action-2",	30,	10)
    list_twenty_stocks.create_stock("Action-3",	50,	15)
    list_twenty_stocks.create_stock("Action-4",	70,	20)
    list_twenty_stocks.create_stock("Action-5",	60,	17)
    list_twenty_stocks.create_stock("Action-6",	80,	25)
    list_twenty_stocks.create_stock("Action-7",	22,	7)
    list_twenty_stocks.create_stock("Action-8",	26,	11)
    list_twenty_stocks.create_stock("Action-9",	48,	13)
    list_twenty_stocks.create_stock("Action-10", 34, 27)
    list_twenty_stocks.create_stock("Action-11", 42, 17)
    list_twenty_stocks.create_stock("Action-12", 110, 9)
    list_twenty_stocks.create_stock("Action-13", 38, 23)
    list_twenty_stocks.create_stock("Action-14", 14, 1)
    list_twenty_stocks.create_stock("Action-15", 18, 3)
    list_twenty_stocks.create_stock("Action-16", 8, 8)
    list_twenty_stocks.create_stock("Action-17", 4, 12)
    list_twenty_stocks.create_stock("Action-18", 10, 14)
    list_twenty_stocks.create_stock("Action-19", 24, 21)
    list_twenty_stocks.create_stock("Action-20", 114, 18)
    return list_twenty_stocks


def all_combinations_studies(num_of_stocks, list_stocks):
    """ Study all combinations,
    complete the list a_combination.elements,
    calculate total_cost and total_recipe for all combinations,
    :param: num_of_stocks is the total nummber of stocks
            list_stocks is the list of objects from the class Stock
    """
# DETAIL DE L'ALGORITME FORCE BRUTE
# Création de la liste (vide) des combinaisons possibles
# Parcours de toutes les combinaisons possibles:
# Boucle i allant de 1 à n:
#   c = 0 (numéro de la combinaison)
#   on va traiter toutes les valeur A1 ou nonA1 au premier tour
#   et les placer dans chacune des combinaisons,
#   puis on traitera toutes les valeurs A2 ou nonA2 au deuxième tour,
#   jusqu'à placer les valeurs An nonAn An nonAn An nonAn ...
#   Boucle j allant de 1 à 2 puissance i:
#       j est le nombre de fois où on va répéter Ai
#       d'une combinaison à l'autre,
#       ou bien le nombre de fois où on va répéter nonAi:
#       on place ainsi un groupe de Ai
#       puis un groupe de nonAi,
#       puis un groupe de Ai
#       puis un groupe de nonAi ...
#           si j impair, l'element vaut Ai et on prend son cout,
#           sinon il vaut nonAi et le cout vaut 0
#           boucle k allant de 1 à 2 ** (N-i)
#               ajouter l'élément Ai ou nonAi à la combinaison numero c
#               augmenter c de 1 pour passer à la combinaison suivante
# Calcul du gain et de la meilleure offre
    p = 2 ** num_of_stocks
    list_of_combinations = Combinations(num_of_stocks)
    for i in range(p):
        list_of_combinations.create_combination(i)
    # Parcours de toutes les combinaisons possibles:
    for i in range(num_of_stocks):
        # c = 0 (numéro de la combinaison)
        # Boucle i allant de 1 à n
        # (on place chaque A1, puis chaque A2, ..., chaque An)
        c = 0
        for j in range(2 ** (i + 1)):
            # Boucle j allant de 1 à 2**i:
            # on place des A1 puis des nonA1,
            # puis des A1 puis des nonA1...
            # si j impair, l'element vaut Ai et on prend son cout,
            # sinon il vaut nonAi et le cout vaut 0
            if j % 2 == 0:
                elt = "A" + str(i+1)
                cost = list_stocks[i].cost
                r = list_stocks[i].recipe
            else:
                elt = "nonA" + str(i+1)
                cost = 0
                r = 0
            for k in range(2 ** (num_of_stocks - i - 1)):
                # boucle k allant de 1 à 2 ** (N-i)
                # ajouter l'élément à la combinaison numero c
                # ajouter
                # c += 1
                list_of_combinations.combinations_list[c].elements.append(elt)
                list_of_combinations.combinations_list[c].total_cost += cost
                list_of_combinations.combinations_list[c].total_recipe += r
                c += 1
    return list_of_combinations


# Calcul du gain et de la meilleure offre
def best_choice_ever(list_of_combinations, total_budget):
    """ Calculate which combination give the best gain
    """
    best_offer = 0
    i = 0
    for combination in list_of_combinations.combinations_list:
        combination.gain = combination.total_recipe - combination.total_cost
        cond1 = combination.gain >= best_offer
        cond2 = combination.total_cost <= total_budget
        if cond1 and cond2:
            best_offer = combination.gain
            c = combination.id
        i += 1
    return c, best_offer


# MAIN
# Calcul pour 5 actions:
answer = "Hello world"
while answer != "1" and answer != "2":
    print("\n Tapez 1 pour effectuer un test avec 5 actions seulement,")
    print("ou tapez 2 trouver la solution avec les 20 actions données: ")
    answer = input()
if answer == "1":
    the_stocks = five_stocks()
    list_stocks = the_stocks.stocks_list
    num_of_stocks = len(list_stocks)
    total_budget = 15
    # debut de l'algorithme qui cherche la meilleure solution
    starting_time = math.floor(time() * 1000)
    list_of_combinations = all_combinations_studies(num_of_stocks, list_stocks)
    c, best_offer = best_choice_ever(list_of_combinations, total_budget)
    ending_time = math.floor(time() * 1000)
    # fin de l'algorithme qui cherche la meilleure solution
    duration = ending_time - starting_time
    f = math.floor(duration / 1000)
    d = duration - f * 1000
    delay = str(f) + "." + str(d) + " secondes"
    print("\n Nombre total de combinaisons: ")
    print(list_of_combinations.num_of_combinations)
    print("\n Meilleur offre: ")
    list_of_combinations.combinations_list[c].display()
    print("\n Temps écoulé pour calculer la meilleure offre:")
    print(delay)
else:
    the_stocks = twenty_stocks()
    list_stocks = the_stocks.stocks_list
    num_of_stocks = len(list_stocks)
    total_budget = 500
    # debut de l'algorithme qui cherche la meilleure solution
    starting_time = math.floor(time() * 1000)
    list_of_combinations = all_combinations_studies(num_of_stocks, list_stocks)
    c, best_offer = best_choice_ever(list_of_combinations, total_budget)
    ending_time = math.floor(time() * 1000)
    # fin de l'algorithme qui cherche la meilleure solution
    duration = ending_time - starting_time
    f = math.floor(duration / 1000)
    d = duration - f * 1000
    delay = str(f) + "." + str(d) + " secondes"
    print("\n Nombre total de combinaisons: ")
    print(list_of_combinations.num_of_combinations)
    print("\n Meilleur offre: ")
    list_of_combinations.combinations_list[c].display()
    print("\n Temps écoulé pour calculer la meilleure offre:")
    print(delay)
# Calcul pour 6 à 22 actions:
answer = "Hello world"
while answer != "1" and answer != "2":
    print("\n Tapez 1 pour effectuer une étude de l'évolution"
          + "du temps d'éxécution pour 12 à 23 actions")
    print("ou tapez 2 pour quitter le programme: ")
    answer = input()
if answer == "1":
    the_stocks = twenty_stocks()
    list_1 = the_stocks.stocks_list
    list_stocks = list_1 + list_1
    num_of_stocks = len(list_stocks)
    total_budget = 500
    n = 12
    number_of_stocks = []
    times_list = []
    answer = "Hello world"
    while n <= 23:
        starting_time = math.floor(time() * 1000)
        list_of_combinations = all_combinations_studies(n, list_stocks)
        c, best_offer = best_choice_ever(list_of_combinations, total_budget)
        ending_time = math.floor(time() * 1000)
        duration = ending_time - starting_time
        f = math.floor(duration / 1000)
        d = duration - f * 1000
        delay = str(f) + "." + str(d) + " secondes"
        times_list.append(delay)
        number_of_stocks.append(n)
        print(f"Nombre d'actions au départ: {n}")
        print("\n Nombre total de combinaisons: ")
        print(list_of_combinations.num_of_combinations)
        print("\n Meilleur offre: ")
        list_of_combinations.combinations_list[c].display()
        print("\n Temps écoulé pour calculer la meilleure offre:")
        print(delay)
        n += 1
    # affichage des temps d'éxécution
    print(number_of_stocks)
    print(times_list)
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour afficher le graphique. "
        answer = input(text)
    plt.scatter(number_of_stocks, times_list, color='black')
    plt.plot(number_of_stocks, times_list, linestyle='dashed', color='red')
    axis = plt.gca()
    axis.set_xlabel("Nombre d'actions étudiées")
    axis.set_ylabel("Temps d'éxécution en secondes")
    plt.title("Evolution du temps d'éxécution de l'algo force brute")
    plt.xlim(10, 25)
    plt.ylim(-100, 1500)
    plt.grid()
    plt.show()
    print("Fin du programme")
else:
    print("Fin du programme.")
