# solution optimisée, avec un algo glouton
# puis en programmation dynamique
from time import time
import math
import csv
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
            stocks_display = stock.name + " coût" + str(stock.cost/digits)
            stocks_display += " pourcentage benefice: " + str(stock.benefit)
            stocks_display += " recette: " + str(stock.recipe/digits)
            stocks_display += "\n efficacité: " + str(stock.efficiency)
            print(stocks_display)
        n = len(self.stocks_list)
        p = 2 ** n
        print(f"il y a {n} actions dans la liste,")
        print(f"et {p} combinaisons possibles avec budget illimité")


class Stock:
    """ actions we can bought
    self.cost is transformed to an integer, digits times the entry
    self.benefit is a float, with 3 digits after point
    self.recipe is an integer, calculate with cost and benefit
    self.efficiency is a float, with 3 digits after point
    :param: name (type: string), cost (type:float), benefit (type: float)
    """

    def __init__(self, name, cost, benefit):
        self.name = name
        print(self.name)
        self.cost = int(digits * cost)
        print(self.cost)
        self.benefit = math.floor(1000 * benefit) / 1000
        self.bought = False
        self.recipe = math.floor(self.cost * (1 + benefit / 100))
        print(self.recipe)
        self.efficiency = math.floor(self.recipe / self.cost * 1000) / 1000
        print(self.efficiency)


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


def dataset_stocks(a_name):
    list_dataset_stocks = Stocks(a_name)
    file_path = 'Datasets/' + a_name + '.csv'
    with open(file_path, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=' ', quotechar=',')
        r = 0
        for row in data_reader:
            if r != 0:
                informations = row[0].split(',')
                try:
                    stock_name = informations[0].replace('Share-', '')
                    stock_cost = int(float(informations[1]))
                    stock_benefice = int(float(informations[2]))
                    if stock_cost > 0 and stock_benefice > 0:
                        list_dataset_stocks.create_stock(stock_name,
                                                         stock_cost,
                                                         stock_benefice)
                    else:
                        print(f"Ligne {r} non prise en compte,"
                              + " le coût ou le bénéfice sont negatifs ou nul")
                except Exception as e:
                    print(f"Problème de lecture dans la ligne {r} du csv")
                    print(e)
            r += 1
    return list_dataset_stocks


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
    starting_time = math.floor(time() * 10000)
    stocks_by_efficiency = sorted(list_of_stocks,
                                  key=lambda stock: stock.efficiency,
                                  reverse=True)
    greedy_combinaison = []
    loaded_costs = 0
    total_recipe = 0
    for stock in stocks_by_efficiency:
        if stock.cost + loaded_costs <= total_budget:
            greedy_combinaison.append(stock)
            loaded_costs += stock.cost
            total_recipe += stock.recipe
    ending_time = math.floor(time() * 10000)
    duration = ending_time - starting_time
    f = math.floor(duration / 10000)
    d = duration - f * 10000
    delay = str(f) + "." + str(d)
    return greedy_combinaison, loaded_costs, total_recipe, delay


def greedy_display(greedy_combinaison, loaded_costs, total_recipe, delay):
    print("Voici la combinaison retenue (algorithme glouton): ")
    for stock in greedy_combinaison:
        print(stock.name)
    the_benefice = (total_recipe - loaded_costs)
    print("Le coût total vaut alors " + str(loaded_costs / digits))
    print("La recette totale vaut: " + str(total_recipe / digits))
    print("Le bénéfice total vaut: " + str(the_benefice / digits))
    print("Programme effectué en " + str(delay) + " secondes")


# PROGRAMMATION DYNAMIQUE
def dynamic_programming(number_of_stocks, total_budget, list_stocks):
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
    starting_time = math.floor(time() * 10000)
    recipe_tabular = []
    total_weight = int(total_budget / digits)
    # First line of the dataframe
    recipe_tabular.append([])
    try:
        for j in range(total_weight + 1):
            actual_cost = int(list_stocks[0].cost / digits)
            if actual_cost > j:
                recipe_tabular[0].append(0)
            else:
                recipe_tabular[0].append(list_stocks[0].recipe)
    except IndexError:
        print(f"Erreur d'index première ligne, j = {j}")
    # Complete the dataframe of recipes get
    try:
        for i in range(1, number_of_stocks):
            recipe_tabular.append([])
            try:
                for j in range(total_weight + 1):
                    value_above = recipe_tabular[i - 1][j]
                    actual_cost = int(list_stocks[i].cost / digits)
                    if actual_cost > j:
                        recipe_tabular[i].append(value_above)
                    else:
                        diff = j - actual_cost
                        left_above = recipe_tabular[i - 1][diff]
                        recipe_to_load = list_stocks[i].recipe
                        stock_to_load = recipe_to_load + left_above
                        m = max(stock_to_load, value_above)
                        recipe_tabular[i].append(m)
            except IndexError:
                print(f"Erreur d'index dans la colonne j = {j}, "
                      + f"sur la ligne i = {i}")
                print(f"Valeurs diff {diff}, value above {value_above},"
                      + f" actual cost {actual_cost}, max {m}")
    except IndexError:
        print(f"Erreur d'index sur la ligne i = {i}")
    ending_time = math.floor(time() * 10000)
    duration = ending_time - starting_time
    f = math.floor(duration / 10000)
    d = duration - f * 10000
    delay = str(f) + "." + str(d)
    return recipe_tabular, delay


def recipe_tabular_display(recipe_tabular):
    """ print the recipe's tabular get by dynamic programming"""
    i = 1
    for line in recipe_tabular:
        print(f"\n Action n° {i}")
        print(line)
        i += 1


def dynamic_prog_display(recipe_tabular, solution, delay):
    # Afficher l'élément recipe_tabular[n-1][w], la recette totale
    total_recipe = 0
    total_cost = 0
    for stock in solution:
        total_cost += stock.cost
        total_recipe += stock.recipe
    print("Voici le coût total: ")
    print(int(total_cost / digits))
    print("Voici la recette totale obtenue: ")
    print(int(total_recipe / digits))
    the_benefice = total_recipe - total_cost
    print("Le bénéfice vaut: " + str(the_benefice / digits))
    print("Programme effectué en " + str(delay) + " secondes")


def finding_solution(recipe_tabular, list_stocks, num_of_stocks, total_budget):
    """ :param: recipe tabular is the tabular made by dynamic programming
                list_stocks is a list of objects from the class Stock
                num_of_stocks is the length of list_of_stocks
                total_budget is an integer, the limit for costs
    """
    # Remontée du tableau pour la programmation dynamique
    # on part de i = nombre d'actions - 1
    # on part de j = w poids limite
    # recette actuelle v = tab [i][j]
    # Tant que i est supérieur ou égal à 0 et v différent de 0:
    #   si v = tab[i-1][j] (pour i différent de 0 !!)
    #       alors on remonte d'une ligne: i devient i - 1
    #   sinon:
    #       l'action i est prise
    #       j devient j - poids de l'action i
    #       i devient i - 1
    #       v devient tab[i][j]
    total_weight = int(total_budget / digits)
    i = num_of_stocks - 1
    j = total_weight
    v = recipe_tabular[i][j]
    solution = []
    while v != 0 and i > 0:
        # print("Traitement action n°" + str(i+1))
        if v == recipe_tabular[i - 1][j]:
            i -= 1
        else:
            actual_cost = int(list_stocks[i].cost / digits)
            j = j - actual_cost
            solution.append(list_stocks[i])
            i -= 1
            v = recipe_tabular[i][j]
    if i == 0 and v != 0:
        solution.append(list_stocks[0])
    print("\n Voici les actions retenues:")
    for item in solution:
        print(item.name)
    return solution


digits = 1000


def main():
    answer = "Hello world"
    while answer != "1" and answer != "2":
        print("\n Tapez 1 pour effectuer un test avec 5 actions seulement,")
        print("ou tapez 2 trouver la solution avec les différentes listes"
              + " d'actions données: ")
        answer = input()
    if answer == "1":
        # Solutions pour 5 actions
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution greedy avec 5 actions: "
            answer = input(text)
        the_stocks = five_stocks()
        list_stocks = the_stocks.stocks_list
        num_of_stocks = len(list_stocks)
        budget = 15 * digits
        combi, load_costs, recipe, delay = greedy_algorithm(budget,
                                                            list_stocks)
        greedy_display(combi, load_costs, recipe, delay)
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution en programmation dynamique"
            text += " avec 5 actions: "
            answer = input(text)
        a_tabular, delay = dynamic_programming(num_of_stocks,
                                               budget,
                                               list_stocks)
        solution = finding_solution(a_tabular, list_stocks,
                                    num_of_stocks, budget)
        dynamic_prog_display(a_tabular, solution, delay)
    else:
        # Solutions pour 20 actions OC
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution greedy avec 20 actions: "
            answer = input(text)
        the_stocks = twenty_stocks()
        list_stocks = the_stocks.stocks_list
        num_of_stocks = len(list_stocks)
        budget = 500 * digits
        combi, load_costs, recipe, delay = greedy_algorithm(budget,
                                                            list_stocks)
        greedy_display(combi, load_costs, recipe, delay)
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution en programmation dynamique"
            text += " avec 20 actions: "
            answer = input(text)
        a_tabular, delay = dynamic_programming(num_of_stocks,
                                               budget,
                                               list_stocks)
        solution = finding_solution(a_tabular, list_stocks,
                                    num_of_stocks, budget)
        dynamic_prog_display(a_tabular, solution, delay)
        # recuperation des datasets
        input("Appuyez sur Entrée pour charger les deux datasets")
        dataset1_stocks = dataset_stocks('dataset1')
        dataset2_stocks = dataset_stocks('dataset2')
        taille1 = len(dataset1_stocks.stocks_list)
        taille2 = len(dataset2_stocks.stocks_list)
        print(f"Nombre d'actions prises en comptes: {taille1} et {taille2}")
        # solution greedy pour le dataset1
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution greedy avec le dataset 1: "
            answer = input(text)
        list_stocks_1 = dataset1_stocks.stocks_list
        num_of_stocks = len(list_stocks_1)
        combi, load_costs, recipe, delay = greedy_algorithm(budget,
                                                            list_stocks_1)
        greedy_display(combi, load_costs, recipe, delay)
        # solution en programmtion dynamique pour le dataset 1
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution en programmation dynamique"
            text += " avec le dataset 1: "
            answer = input(text)
        a_tabular, delay = dynamic_programming(num_of_stocks,
                                               budget,
                                               list_stocks_1)
        solution = finding_solution(a_tabular, list_stocks_1,
                                    num_of_stocks, budget)
        dynamic_prog_display(a_tabular, solution, delay)
        # solution greedy pour le dataset 2
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution greedy avec le dataset 2: "
            answer = input(text)
        list_stocks_2 = dataset2_stocks.stocks_list
        num_of_stocks = len(list_stocks_2)
        combi, load_costs, recipe, delay = greedy_algorithm(budget,
                                                            list_stocks_2)
        greedy_display(combi, load_costs, recipe, delay)
        # solution en programmtation dynamique pour le dataset 2
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour la solution en programmation dynamique"
            text += " avec le dataset 2: "
            answer = input(text)
        a_tabular, delay = dynamic_programming(num_of_stocks,
                                               budget,
                                               list_stocks_2)
        solution = finding_solution(a_tabular, list_stocks_2,
                                    num_of_stocks, budget)
        dynamic_prog_display(a_tabular, solution, delay)
    while answer != "1" and answer != "2":
        print("\n Tapez 1 pour effectuer une étude de l'évolution "
              + "du temps d'éxécution pour différentes listes d'actions")
        print("ou tapez 2 pour quitter le programme: ")
        answer = input()
    if answer == "1":
        # evolution en programmation dynamique
        list_stocks = list_stocks_1 + list_stocks_2
        num = len(list_stocks)
        print("Nombre total d'actions prises en compte"
              + f" avec les deux datasets: {num}")
        list_stocks_3 = list_stocks_1 + list_stocks_2
        for i in range(3):
            list_stocks_3 += list_stocks_1 + list_stocks_2
        stocks_used_numbers = []
        list_of_times = []
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour lancer les 20 répétitions en prog dynamique"
            answer = input(text)
        for i in range(20):
            list_stocks += list_stocks_3
            num_of_stocks = len(list_stocks)
            print("Voici la solution en programmation dynamique"
                  + f" avec {num_of_stocks} actions: ")
            a_tabular, delay = dynamic_programming(num_of_stocks,
                                                   budget,
                                                   list_stocks)
            solution = finding_solution(a_tabular, list_stocks,
                                        num_of_stocks, budget)
            dynamic_prog_display(a_tabular, solution, delay)
            list_of_times.append(delay)
            stocks_used_numbers.append(num_of_stocks)
        print(stocks_used_numbers)
        print(list_of_times)
        plt.scatter(stocks_used_numbers, list_of_times, color='black')
        plt.plot(stocks_used_numbers, list_of_times,
                 linestyle='dashed', color='red')
        axis = plt.gca()
        axis.set_xlabel("Nombre d'actions étudiées")
        axis.set_ylabel("Temps d'éxécution en secondes")
        plt.title("Evolution du temps d'éxécution en programmation dynamique")
        plt.grid()
        plt.show()
        # evolution avec les algo glouton
        list_stocks_4 = list_stocks_1 + list_stocks_2
        for i in range(20000):
            list_stocks_4 += list_stocks_1 + list_stocks_2
        greedy_times_list = []
        stocks_used_numbers = []
        answer = "Hello world"
        while answer != "":
            text = "Appuyez sur la touche 'Entrée' "
            text += "pour lancer les 10 répétitions avec l'algo glouton"
            answer = input(text)
        for i in range(20):
            list_stocks += list_stocks_4
            num_of_stocks = len(list_stocks)
            print(f"Voici la solution greedy avec {num_of_stocks} actions")
            combi, load_costs, recipe, delay = greedy_algorithm(budget,
                                                                list_stocks)
            greedy_display(combi, load_costs, recipe, delay)
            greedy_times_list.append(delay)
            stocks_used_numbers.append(num_of_stocks)
        print(stocks_used_numbers)
        print(greedy_times_list)
        plt.scatter(stocks_used_numbers, greedy_times_list, color='black')
        plt.plot(stocks_used_numbers, greedy_times_list,
                 linestyle='dashed', color='red')
        axis = plt.gca()
        axis.set_xlabel("Nombre d'actions étudiées")
        axis.set_ylabel("Temps d'éxécution en secondes")
        plt.title("Evolution du temps d'éxécution avec l'algo glouton")
        plt.grid()
        plt.show()
        print("Fin du programme.")
    else:
        print("Fin du programme.")


if __name__ == "__main__":
    main()
