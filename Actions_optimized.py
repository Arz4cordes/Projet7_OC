# solution optimisée, avec un algo glouton
# puis en programmation dynamique
from time import time
import math
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


# Entrée des différentes actions et du budget total
def five_stocks():
    list_of_five_stocks = Stocks("Liste de 5 actions")
    list_of_five_stocks.create_stock("Action-1", 12, 25)
    list_of_five_stocks.create_stock("Action-2",	2,	150)
    list_of_five_stocks.create_stock("Action-3",	1,	200)
    list_of_five_stocks.create_stock("Action-4",	2,	100)
    list_of_five_stocks.create_stock("Action-5",	4,	150)
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


def greedy_algorithm(total_budget, list_of_stocks):
    # Trier Stocks.stocks_list par efficacité (efficiency)
    # initialiser la liste combinaison
    # coût embarqué = 0
    # benef total = 0
    # Pour chaque action dans les actions triées:
    #   si l'action vérifie coût + coût embaqué <= coût total:
    #       ajouter l'action à la combinaison
    #       ajouter le coût au coût embarqué
    #       ajouter la recette au benef total
    # Afficher la combinaison retenue, le coût total et le benef total
    starting_time = math.floor(time() * 1000)
    stocks_by_efficiency = sorted(list_of_stocks,
                                  key=lambda stock: stock.efficiency,
                                  reverse=True)
    for stock in stocks_by_efficiency:
        print(stock.name + str(stock.recipe))
    greedy_combinaison = []
    loaded_costs = 0
    total_recipe = 0
    for stock in stocks_by_efficiency:
        if stock.cost + loaded_costs <= total_budget:
            greedy_combinaison.append(stock)
            loaded_costs += stock.cost
            total_recipe += stock.recipe
    ending_time = math.floor(time() * 1000)
    duration = ending_time - starting_time
    f = math.floor(duration / 1000)
    d = duration - f * 1000
    delay = str(f) + "." + str(d)
    return greedy_combinaison, loaded_costs, total_recipe, delay


def greedy_display(greedy_combinaison, loaded_costs, total_recipe, delay):
    print("Voici la combinaison retenue (algorithme glouton): ")
    for stock in greedy_combinaison:
        print(stock.name)
    the_benefice = math.floor(1000 * (total_recipe - loaded_costs)) / 1000
    print("Le coût total vaut alors " + str(loaded_costs))
    print("La recette totale vaut: " + str(total_recipe))
    print("Le bénéfice total vaut: " + str(the_benefice))
    print("Programme effectué en " + str(delay) + " secondes")


# PROGRAMMATION DYNAMIQUE
def dynamic_programming(number_of_stocks, total_budget, list_of_stocks):
    # n nombre total d'actions
    # w coût maximum (nombre entier)
    # recipe_tabular est le tableau qui présente les recettes
    #   en appliquant la programmation dynamique
    # On remplit la première ligne (Action 1):
    #   boucle i de 0 à w avec:
    #       0 si coût A1 > i
    #       coût A1 sinon
    # On ajoute la ligne 1 à recipe_tabular (cas j = 0)
    # On remplit les lignes suivantes:
    # boucle j de 1 à n-1 (Action numéro j):
    #   ajouter une liste vide [] à recipe_tabular
    #   boucle i de 0 à w (poids i du sac à dos):
    #       nommons value_above l'élément de rang [i] de la liste [j - 1]
    #           de recipe_tabular
    #       si coût A(j) > i:
    #           alors ajouter l'élément above dans la liste [j]
    #           de recipe_tabular
    #       sinon:
    #           nommons diff l'écart i - coût A(j)
    #           nommons left_above la valeur du rang [diff] de la liste [j - 1]
    #               de recipe_tabular
    #           nommons recipe_to_load la recette A (j)
    #           nommons stock_to_load la somme actual_recipe + left_above
    #           ajouter dans la liste [j] de recipe_tabular
    #           le max entre value_above et stock_to_load
    starting_time = math.floor(time() * 1000)
    recipe_tabular = []
    # First line of the dataframe
    recipe_tabular.append([])
    for i in range(total_budget + 1):
        if list_of_stocks[0].cost > i:
            recipe_tabular[0].append(0)
        else:
            recipe_tabular[0].append(list_of_stocks[0].recipe)
    # Complete the dataframe of recipes get
    for j in range(1, number_of_stocks):
        recipe_tabular.append([])
        text = "Traitement de l'action numéro " + str(j + 1)
        text += " , valeur " + str(list_of_stocks[j].recipe)
        print(text)
        for i in range(total_budget + 1):
            value_above = recipe_tabular[j - 1][i]
            if list_of_stocks[j].cost > i:
                recipe_tabular[j].append(value_above)
            else:
                diff = i - list_of_stocks[j].cost
                left_above = recipe_tabular[j - 1][diff]
                recipe_to_load = list_of_stocks[j].recipe
                stock_to_load = recipe_to_load + left_above
                m = max(stock_to_load, value_above)
                m = math.floor(1000 * m) / 1000
                recipe_tabular[j].append(m)
    ending_time = math.floor(time() * 1000)
    duration = ending_time - starting_time
    f = math.floor(duration / 1000)
    d = duration - f * 1000
    delay = str(f) + "." + str(d)
    return recipe_tabular, delay


def dynamic_prog_display(recipe_tabular, num_of_stocks, total_budget, delay):
    # Afficher l'élément recipe_tabular[n-1][w], la recette totale
    for line in recipe_tabular:
        print(line)
    print("Voici la recette totale obtenue: ")
    print(recipe_tabular[num_of_stocks - 1][total_budget])
    print("Programme effectué en " + str(delay) + " secondes")


def main():
    # Solutions pour 5 actions
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution greedy avec 5 actions: "
        answer = input(text)
    the_stocks = five_stocks()
    list_stocks = the_stocks.stocks_list
    num_of_stocks = len(list_stocks)
    budget = 15
    combi, load_costs, recipe, delay = greedy_algorithm(budget, list_stocks)
    greedy_display(combi, load_costs, recipe, delay)
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution en programmation dynamique avec 5 actions: "
        answer = input(text)
    a_tabular, delay = dynamic_programming(num_of_stocks, budget, list_stocks)
    dynamic_prog_display(a_tabular, num_of_stocks, budget, delay)
    # Solutions pour 20 actions OC
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution greedy avec 20 actions: "
        answer = input(text)
    the_stocks = twenty_stocks()
    list_stocks = the_stocks.stocks_list
    num_of_stocks = len(list_stocks)
    budget = 500
    combi, load_costs, recipe, delay = greedy_algorithm(budget, list_stocks)
    greedy_display(combi, load_costs, recipe, delay)
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution en programmation dynamique avec 20 actions: "
        answer = input(text)
    a_tabular, delay = dynamic_programming(num_of_stocks, budget, list_stocks)
    dynamic_prog_display(a_tabular, num_of_stocks, budget, delay)


if __name__ == "__main__":
    main()
