import random
import math

class Player:
    "Player stats"

    players = []
    #stocks refer to quantity of given stock. money is available money. name is chosen by user
    def __init__(self, name = "", money = 5000):
        self.name = name
        self.money = money
        self.stocks = {
            "Gold": 50,
            "Silver": 0,
            "Oil": 0,
            "Bonds": 0,
            "Grain": 0,
            "Industrial": 0
            }

    #Creates user chosen number of bots (1 - 8)
    def create_bots():
        num_bots = Menu.ask_question("How many bots would you like to play? Choose between 1 - 8.\n", range(1, 8))
        return num_bots

    #Creates user chosen number of human players (2 to 8)
    def create_humans():
        num_humans = Menu.ask_question("How many people are playing? Choose between 2 - 8.\n", range(2, 8))
        return num_humans

    #Creates names for all bot + human players
    def name_player(num_bots, num_humans):
        total_players = num_bots + num_humans
        for num in range(1, total_players+1):
            player = Player(name=Menu.ask_question(f"What is Player {num}'s name?\n"))
            print(f"{player.name} has {player.money} bucks.")
            print(f"Player {num} is now named: {player.name}")
            Player.players.append(player)

    #provide the (stock name, price of stock, amount of money player has) 
    def buy_stock(player):
        current_prices = []
        for num in range(0, 6):
            stock_price = Stock.stocks[num].value
            Player.current_prices.append(stock_price)
        if Player.players[player].money < min(current_prices):
            print("You can't afford any stocks")
        else:
            buy_name = Menu.ask_question("Which stock would you like to buy?\n", Stock.stock_name).capitalize()
            max_purchase = math.trunc(Player.players[player].money/stock_price)
            print(f"You can buy {max_purchase} share(s) of {buy_name}.")
            buy_number = Menu.ask_question("How many shares do you wish to purchase?", range(0,max_purchase))
            Player.players[player].money -= buy_number * stock_price
            Player.players[player].stocks[buy_name] += buy_number

    #provide the (stock name, price of stock, amount of stock player has)
    def sell_stock(player):
        can_sell = []
        for k, v in Player.players[player].stocks:
            if v > 0:
                Player.can_sell.append(v)
        if can_sell is False:
            print("Yoou don't have any stocks to sell!")
        else:
            sell_name = Menu.ask_question("Which stock would you like to sell?", can_sell).capitalize()
            max_sell = Player.players[player].stock[sell_name]
            sell_amount = Menu.ask_question(f"How many shares of {sell_name} do you want to sell?", range(0, max_sell))
            Player.players[player].money += sell_amount * Stock.stocks[sell_name].value

class Bot(Player):
    "All actions for bots"

    def __init__(self):
        pass

    def buy_stock():
        pass
    
    def sell_stock():
        pass

class Stock:
    "Stock value"

    #Change stock names here:
    stock_name = ["Gold", "Silver", "Oil", "Bonds", "Grain", "Industrial"]

    #All stock values during gameplay goes here after create_stocks() runs
    stocks = []

    #Set stock starting cost here:
    def __init__(self, name, value = 100):
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

    #Displays opening message with basic game rules
    def welcome_message():
        pass

    #Displays current players stats
    def player_info(player):
        p_amount = vars(Player.players[player])
        quantity = []
        for key, value in p_amount.items():
            if key != "name":
                quantity.append(value)
        
        print(f"{Player.players[player].name}'s Stats:")
        print(f"Money{str(quantity[0]).rjust(10,'-')}")
        for i, v in enumerate(Stock.stock_name):
            print(f"{str(Stock.stocks[i].name).ljust(10,'-')}-{quantity[i+1]}")

    #Displays current stock prices
    def stock_info():
        print("Stock Prices:")
        for i, v in enumerate(Stock.stock_name):
            print(f"{str(Stock.stocks[i].name).ljust(10,'-')}-{Stock.stocks[i].value}")

    def set_rounds():
        rounds = Menu.ask_question("How many rounds would you like to play? 1 - 1000 \n", Menu.amount)
        return rounds

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
Player.name_player(0,2)
Menu.stock_info()
Menu.player_info(1)    

#CHANGE: list comprehension for any empty lists using standard for loops