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
        print("\n Combinaison: ")
        print(self.elements)
        print("Coût total:")
        print(self.total_cost)
        print("Recette: ")
        print(self.total_recipe)
        


stock1 = Stocks("action 1", 35, 8)
stock2 = Stocks("action 2", 25, 12)
stock2 = Stocks("action 3", 45, 3)
stock2 = Stocks("action 4", 30, 7)
stock2 = Stocks("action 5", 20, 10)
stock2 = Stocks("action 6", 50, 5)
total_budget = 100

for stock in Stocks.stocks_list:
    print(stock.name, " coût: ", stock.cost, " pourcentage benefice: ", stock.benefit, " recette: ", stock.recipe)

n = len(Stocks.stocks_list)
p = 2 ** n
print(f"il y a {n} actions dans la liste, et {p} combinaisons possibles avec budget illimité")

# boucle i allant de 1 à p
    # initier les combinaisons avec le numéro i
for i in range(p):
    combination = Combinations(i, [])

# c = 0 (numéro de la combinaison)

# Boucle i allant de 1 à n (on place A1, puis A2, puis A3...)
    # Boucle j allant de 1 à 2**i: on place des A1 puis des nonA1 puis des A1 puis des nonA1...
        # si j impair, l'element vaut Ai et on prend son cout, sinon il vaut nonAi et le cout vaut 0
            # boucle k allant de 1 à 2 ** (N-i)
                # ajouter l'élément à la combinaison numero c
                # ajouter 
                # # c += 1
for i in range(n):
    c = 0
    for j in range(2 ** i):
        if j%2 == 0:
            element = "non A" + str(i+1)
            the_cost = 0
            the_recipe = 0
        else:
            element = "A" + str(i+1)
            the_cost = Stocks.stocks_list[i - 1].cost
            the_recipe = Stocks.stocks_list[i - 1].recipe
        for k in range(2 **(n - i)):
            Combinations.combinations_list[c].elements.append(element)
            Combinations.combinations_list[c].total_cost += the_cost
            Combinations.combinations_list[c].total_recipe += the_recipe
            c += 1

best_offer = 0
# Calcul du gain et de la meilleure offre
for combination in Combinations.combinations_list:
    combination.gain = combination.total_recipe - combination.total_cost
    if combination.gain >= best_offer and combination.total_cost <= 100:
        best_offer = combination.gain

print(best_offer)
# test: afficher toutes les combinaisons, budget illimité
print("\n AFFICHAGE DE TOUTES LES COMBINAISONS \n")
for combination in Combinations.combinations_list:
    combination.display()

print("\n AFFICHAGE DE TOUTES LES OFFRES AVEC 100 EUROS DE BUDGET \n")
for combination in Combinations.combinations_list:
    if combination.total_cost <= 100:
        combination.display()
        print("GAIN: " + str(combination.gain))
        if combination.gain == best_offer:
            print("MEILLEURE OFFRE !")
