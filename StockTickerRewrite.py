import random

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

        #Subclass Humans
        #Subclass Bots

    #Creates user chosen number of bots (1 - 8)
    def create_bots():
        num_bots = ask_question("How many bots would you like to play? Choose between 1 - 8.\n", range(1, 8))
        return num_bots

    #Creates user chosen number of human players (2 to 8)
    def create_humans():
        num_humans = ask_question("How many people are playing? Choose between 2 - 8.\n", range(2, 8))
        return num_humans

    #Creates names for all bot + human players
    def name_player(total_players):
        total_players = 5
        for num in range(1, total_players+1):
            # player = Player(name=f"Player {num}")
            player = Player(name=ask_question(f"What is Player {num}'s name?\n"))
            print(f"{player.name} has {player.money} bucks.")
            print(f"Player {num} is now named: {player.name}")
            Player.players.append(player)

    #provide the (stock name, price of stock, amount of money player has) 
    def buy_stock(stock, cost, player_money):
        pass

    #provide the (stock name, price of stock, amount of stock player has)
    def sell_stock(stock, cost, player_quantity):
        pass

class Stock:
    "Stock value"

    #Change stock names here:
    stock_name = ["Gold", "Silver", "Oil", "Bonds", "Grain", "Industrial"]
    #All stock data goes here after create_stocks() runs
    stocks = []

    #Set stock starting cost here:
    def __init__(self, name, value = 195):
        self.name = name
        self.value = value

    #Create list of stocks with data based on Stock class
    def create_stocks():
        for num in range(0, 6):
            print(f"Now working on {Stock.stock_name[num]}")
            stock = Stock(name=Stock.stock_name[num])
            Stock.stocks.append(stock)
            print(Stock.stocks[num].name)

    #Called from roll(), handles adding to stock value
    def increase_value(stock, amount):
        stock_index = Stock.stock_name.index(stock)
        #Called from increase_value(), handles doubling player held stock quantities
        def double_stock(stock):
            #stock value reset to 100 (default), double quantity of players holding stock
            print("Now in double_stock()")

        print("now in increase_value()")
        
        Stock.stocks[stock_index].value = Stock.stocks[stock_index].value + amount
        if Stock.stocks[stock_index].value > 195:
            double_stock(stock)

    #Called from roll(), handles subtracting from stock value
    def decrease_value(stock, amount):
        stock_index = Stock.stock_name.index(stock)
        #Called from decrease_value(), handles removing all of selected stock from player inventory
        def split_stock(stock):
            #stock value reset to 100 (default), set quantity to 0 of players holding stock
            print("Now in split_stock()")

        print("Now in decrease_value()")
        Stock.stocks[stock_index].value = Stock.stocks[stock_index].value - amount
        print(Stock.stocks[stock_index].value)
        if Stock.stocks[stock_index].value < 5:
            split_stock(stock)

    def dividend(stock, amount):
        #all players with selected stock get quantity multiplied by amount
        print("Now in dividend()")

class Dice:
    "Dice properties"

    stock_name = Stock.stock_name
    action = ["Up", "Down", "Dividend"]
    amount = [5, 10, 20]

    #Rolls 3 dice (stock_name, action, amount) and prints the results to the screen.
    def roll():
        stock = random.choice(Dice.stock_name)
        action = random.choice(Dice.action)
        amount = random.choice(Dice.amount)
        print(stock, action, amount)

        #Make appropriate changes to stock based on roll
        if action == Dice.action[0]:
            Stock.increase_value(stock, amount)
        elif action == Dice.action [1]:
            Stock.decrease_value(stock, amount)
        else:
            Stock.dividend(stock, amount)

class Menu:
    "All menu screens"
    stocks = Stock.stock_name #Answer for stock name
    action = ["Buy", "Sell", "Done", ""]
    amount = [range(1-1000)]

    def main_screen():
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

Stock.create_stocks()
Dice.roll()
