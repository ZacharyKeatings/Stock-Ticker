class Player:
    "Player stats"
    players = []
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

    #Creates user chosen number of bots (0 - 8)
    def create_bots(num_bots):
        pass

    #Creates user chosen number of human players (2 to 8)
    def create_humans(num_humans):
        pass

    def name_players(player):
        name = ask_question(f"What is {player}'s name?\n")
        return name

    def buy_stock(stock, amount):
        pass

    def sell_stock(stock, amount):
        pass

    

class Stock:
    "Stock value"

    gold_value = 100
    silver_value = 100
    oil_value = 100
    bonds_value = 100
    grain_value = 100
    industrial_value = 100

    def __init__(self, name, value = 100):
        self.name = name
        self.value = value

    def increase_value(stock):
        pass

    def decrease_value(stock):
        pass

    def double_stock(stock):
        pass

    def split_stock(stock):
        pass

class Dice:
    "Dice properties"

    stock_name = []
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

human_players = 0
bot_players = 0
num_players = 5 #Add human and bot for this value in the future
current_player = 1
print(Stock.gold)
#Creating number of players as chosen by user based on Player class, as well as choosing names.
#try using for loop and replace player# with i placeholder. shorter code?
while current_player <= num_players:
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
