class Player:
    "Player stats"

    #stocks refer to quantity of given stock. money is available money. name is chosen by user
    def __init__(self, name = "", money = 5000, gold = 0, silver = 0, oil = 0, bonds = 0, grain = 0, industrial = 0):
        self.name = name
        self.money = money
        self.gold = gold
        self.silver = silver
        self.oil = oil
        self.bonds = bonds
        self.grain = grain
        self.industrial = industrial

    #Creates user chosen number of bots (1 - 8)
    def create_bots():
        num_bots = ask_question("How many bots would you like to play? Choose between 1 - 8.\n", range(1, 8))
        return num_bots

    #Creates user chosen number of human players (2 to 8)
    def create_humans():
        num_humans = ask_question("How many people are playing? Choose between 2 - 8.\n", range(2, 8))
        return num_humans

    def name_players(player):
        name = ask_question(f"What is {player}'s name?\n")
        return name

    #provide the (stock name, price of stock, amount of money player has) 
    def buy_stock(stock, cost, player_money):
        pass

    #provide the (stock name, price of stock, amount of stock player has)
    def sell_stock(stock, cost, player_quantity):
        pass

class Stock:
    "Stock value"

    #Change stock names here:
    stock_list = ["Gold", "Silver", "Oil", "Bonds", "Grain", "Industrial"]

    def __init__(self, name, value = 100):
        self.name = name
        self.value = value

    def increase_value(stock, amount):
        #If stock value >= 200, double_stock(stock)
        pass

    def decrease_value(stock, amount):
        #If stock value <= 0, split_stock(stock)
        pass

    def double_stock(stock):
        #stock value reset to 100 (default), double quantity of players holding stock
        pass

    def split_stock(stock):
        #stock value reset to 100 (default), set quantity to 0 of players holding stock
        pass

class Dice:
    "Dice properties"

    stock_name = Stock.stock_list
    action = ["Up", "Down", "Dividend"]
    amount = [5, 10, 20]

    def __init__(self, name, value = 100):
        self.name = name
        self.value = value

    def roll():
        pass

#test = ask_question("What question?", ["y","n"])
def ask_question(question, answers=None):
    asking = True
    while asking:
        response = input(f"{question}")
        if answers is None:
            return response
        else:
            asking = False if response not in answers else True
    return response

#Do you want to play with bots?
#if yes, call create_bots()
#if no, call create_humans()

##########
#Create the stocks:
stock1 = Stock(Stock.stock_list[0])
stock2 = Stock(Stock.stock_list[1])
stock3 = Stock(Stock.stock_list[2])
stock4 = Stock(Stock.stock_list[3])
stock5 = Stock(Stock.stock_list[4])
stock6 = Stock(Stock.stock_list[5])
##########

print(Dice.stock_name)

##########
#Create the player placeholder:
# player1 = Player()
# player2 = Player()
# player3 = Player()
# player4 = Player()
# player5 = Player()
# player6 = Player()
# player7 = Player()
# player8 = Player()
##########

human_players = 5
bot_players = 0
total_players = human_players + bot_players
current_player = 1

#Creating number of players as chosen by user based on Player class, as well as choosing names.
while current_player <= total_players:
    if current_player == 1:
        #Player 1
        player1 = Player()
        player1.name = Player.name_players("Player 1")
        print(f"{player1.name} has {player1.money} bucks.")
        current_player += 1
        print(f"{current_player}")
    elif current_player == 2:
        #player 2
        player2 = Player()
        player2.name = Player.name_players("Player 2")
        print(f"{player2.name} has {player2.money} bucks.")
        current_player += 1
        print(f"{current_player}")
    elif current_player == 3:
        #Player 3
        player3 = Player()
        player3.name = Player.name_players("Player 3")
        print(f"{player3.name} has {player3.money} bucks.")
        current_player += 1
        print(f"{current_player}")
    elif current_player == 4:
        #Player 4
        player4 = Player()
        player4.name = Player.name_players("Player 4")
        print(f"{player4.name} has {player4.money} bucks.")
        current_player += 1
        print(f"{current_player}")
    elif current_player == 5:
        #Player 5
        player5 = Player()
        player5.name = Player.name_players("Player 5")
        print(f"{player5.name} has {player5.money} bucks.")
        current_player += 1
        print(f"{current_player}")
    elif current_player == 6:
        #Player 6
        player6 = Player()
        player6.name = Player.name_players("Player 6")
        print(f"{player6.name} has {player6.money} bucks.")
        current_player += 1
        print(f"{current_player}")
    elif current_player == 7:
        #Player 7
        player7 = Player()
        player7.name = Player.name_players("Player 7")
        print(f"{player7.name} has {player7.money} bucks.")
        current_player += 1
        print(f"{current_player}")
    elif current_player == 8:
        #Player 8
        player8 = Player()
        player8.name = Player.name_players("Player 8")
        print(f"{player8.name} has {player8.money} bucks.")
        print(f"{current_player}")
        current_player += 1
