# solution optimisée, avec un algo glouton
# puis en programmation dynamique
from time import time
import math
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
        self.recipe = math.floor(1000 * cost * (1 + benefit / 100)) / 1000
        self.efficiency = self.recipe / self.cost
        return Stocks.stocks_list.append(self)

    def display(self):
        # Affichage des différentes actions et du nombre total de combinaison
        for stock in Stocks.stocks_list:
            stocks_display = stock.name + " coût" + str(stock.cost)
            stocks_display += " pourcentage benefice: " + str(stock.benefit)
            stocks_display += " recette: " + str(stock.recipe)
            stocks_display += "\n efficacité: " + str(stock.efficiency)
            print(stocks_display)
        n = len(Stocks.stocks_list)
        p = 2 ** n
        print(f"il y a {n} actions dans la liste,")
        print(f"et {p} combinaisons possibles avec budget illimité")


# Entrée des différentes actions et du budget total
def five_stocks():
    Stocks.stocks_list = []
    stock1 = Stocks("Action-1", 12, 25)
    stock2 = Stocks("Action-2",	2,	150)
    stock3 = Stocks("Action-3",	1,	200)
    stock4 = Stocks("Action-4",	2,	100)
    stock5 = Stocks("Action-5",	4,	150)


def twenty_stocks():
    Stocks.stocks_list = []
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
    return Stocks.stocks_list


def greedy_algorithm(total_budget):
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
    starting_time = time()
    stocks_by_efficiency = sorted(Stocks.stocks_list,
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
    ending_time = time()
    delay = ending_time - starting_time
    return greedy_combinaison, loaded_costs, total_recipe, delay


def greedy_display(greedy_combinaison, loaded_costs, total_recipe, delay):
    print("Voici la combinaison retenue (algorithme glouton): ")
    for stock in greedy_combinaison:
        print(stock.name)
    print("Le coût total vaut alors " + str(loaded_costs))
    print("La recette totale vaut: " + str(total_recipe))
    print("Le bénéfice total vaut: " + str(total_recipe - loaded_costs))
    print("Programme effectué en " + str(delay) + " secondes")


# PROGRAMMATION DYNAMIQUE
def dynamic_programming(number_of_stocks, total_budget):
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
    starting_time = time()
    recipe_tabular = []
    # First line of the dataframe
    recipe_tabular.append([])
    for i in range(total_budget + 1):
        if Stocks.stocks_list[0].cost > i:
            recipe_tabular[0].append(0)
        else:
            recipe_tabular[0].append(Stocks.stocks_list[0].recipe)
    # Complete the dataframe of recipes get
    for j in range(1, number_of_stocks):
        recipe_tabular.append([])
        print("Traitement de l'action numéro " + str(j + 1) + " , valeur " + str(Stocks.stocks_list[j].recipe))
        for i in range(total_budget + 1):
            value_above = recipe_tabular[j - 1][i]
            if Stocks.stocks_list[j].cost > i:
                recipe_tabular[j].append(value_above)
            else:
                diff = i - Stocks.stocks_list[j].cost
                left_above = recipe_tabular[j - 1][diff]
                recipe_to_load = Stocks.stocks_list[j].recipe
                stock_to_load = recipe_to_load + left_above
                m = max(stock_to_load, value_above)
                recipe_tabular[j].append(m)
    ending_time = time()
    delay = starting_time - ending_time
    return recipe_tabular, delay


def dynamic_prog_display(recipe_tabular, number_of_stocks, total_budget, delay):
    # Afficher l'élément recipe_tabular[n-1][w], la recette totale
    for line in recipe_tabular:
        print(line)
    print("Voici la recette totale obtenue: ")
    print(recipe_tabular[number_of_stocks - 1][total_budget])
    print("Programme effectué en " + str(delay) + " secondes")


def main():
    # Solutions pour 5 actions
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution greedy avec 5 actions: "
        answer = input(text)
    five_stocks()
    number_of_stocks = len(Stocks.stocks_list)
    total_budget = 15
    greedy_combi, load_costs, recipe, delay = greedy_algorithm(total_budget)
    greedy_display(greedy_combi, load_costs, recipe, delay)
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution en programmation dynamique avec 5 actions: "
        answer = input(text)
    recipe_tabular, delay = dynamic_programming(number_of_stocks, total_budget)
    dynamic_prog_display(recipe_tabular, number_of_stocks, total_budget, delay)
    # Solutions pour 20 actions OC
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution greedy avec 20 actions: "
        answer = input(text)
    twenty_stocks()
    number_of_stocks = len(Stocks.stocks_list)
    total_budget = 500
    greedy_combi, load_costs, recipe, delay = greedy_algorithm(total_budget)
    greedy_display(greedy_combi, load_costs, recipe, delay)
    answer = "Hello world"
    while answer != "":
        text = "Appuyez sur la touche 'Entrée' "
        text += "pour la solution en programmation dynamique avec 20 actions: "
        answer = input(text)
    recipe_tabular, delay = dynamic_programming(number_of_stocks, total_budget)
    dynamic_prog_display(recipe_tabular, number_of_stocks, total_budget, delay)


if __name__ == "__main__":
    main()
