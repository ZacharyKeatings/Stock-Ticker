import random
import math

class Player:
    "Player stats"

    players = []

    def __init__(self, name = "", money = 5000):
        """stocks refer to quantity of given stock. money is available money. name is chosen by user"""
        self.name = name
        self.money = money
        self.stocks = {
            "Gold": 0,
            "Silver": 0,
            "Oil": 0,
            "Bonds": 0,
            "Grain": 0,
            "Industrial": 0
            }

    def create_bots():
        """Creates user selected number of bots (1 - 8)"""
        num_bots = int(Menu.ask_question("How many bots would you like to play? Choose between 1 - 8.\n", Menu.num_player))
        return num_bots

    def create_humans():
        """Creates user chosen number of human players (2 to 8)"""
        num_humans = Menu.ask_question("How many people are playing? Choose between 2 - 8.\n", range(2, 8))
        return int(num_humans)

    def name_player(num_bots, num_humans):
        """Creates names for all bot + human players"""
        total_players = num_bots + num_humans
        for num in range(1, total_players+1):
            player = Player(Menu.ask_question(f"What is Player {num}'s name?\n", Menu.name))
            print(f"Player {num} is now named: {player.name}")
            Player.players.append(player)
        return total_players

    def current_prices(player):
        """Checks if player can afford any stocks."""
        current_prices = []
        for num in range(0, 6):
            stock_price = Stock.stocks[num].value
            current_prices.append(stock_price)
        if Player.players[player].money < min(current_prices):
            print("You can't afford any stocks")
            return False
        else:
            return True

    def buy_stock(player):
        """User chooses which stock to buy and the quantity"""
    
        def max_purchase(stock_name):
            """Defines the highest quantity of selected stock user can purchase with current funds"""
            index = Stock.stock_index(buy_name)
            max_purchase = math.trunc(Player.players[player].money/Stock.stocks[index].stock_price)
            print(f"You can buy {max_purchase} share(s) of {stock_name}.")
            return max_purchase

        price_check = Player.current_prices(player)
        while price_check:        
            buy_name = Menu.ask_question("Which stock would you like to buy?\n", Menu.stocks).capitalize()
            while int(max_purchase) >= 1:
                max_purchase = max_purchase(buy_name)
                buy_number = Menu.ask_question("How many shares do you wish to purchase?", range(0,max_purchase))
                buy_number = int(buy_number)
                Player.players[player].money -= buy_number * Stock.stocks.index(buy_name) 
                Player.players[player].stocks[buy_name] += buy_number

    def sell_stock(player):
        """User choose which stock to sell and the quantity"""
        can_sell = []
        for key in Player.players[player].stocks:
            value = Player.players[player].stocks[key]
            if value > 0:
                can_sell.append(value)
        if can_sell is False:
            print("You don't have any stocks to sell!")
        else:
            sell_name = Menu.ask_question("Which stock would you like to sell?", can_sell).capitalize()
            sell_index = Stock.stock_name.index(sell_name)
            max_sell = Player.players[player].stocks[sell_name]
            sell_amount = Menu.ask_question(f"How many shares of {sell_name} do you want to sell?", range(0, max_sell))
            sell_amount = int(sell_amount)
            Player.players[player].money += sell_amount * Stock.stocks[sell_index].value
            Player.players[player].stocks[sell_name] -= sell_amount

    def dividend(stock, div_roll):
        """Called from Dice.roll(), handles issuing players holding selected stock bonus funds"""
        #all players with selected stock get quantity multiplied by Dice.roll().amount
        print("Now in dividend()")
        dividend = (div_roll / 10) + 1
        #Check that rolled stock value is >=100:
        if Stock.stocks[stock].value >= 100:
            for num in enumerate(Menu.num_players):
                Player.players[num].stocks[stock] *= dividend
        else:
            return None

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

    def __init__(self, name, value = 100):
        """Sets stock name and the stock value"""
        self.name = name
        self.value = value

    def create_stocks():
        """append Stock.stock with stock names from Stock.stock_name"""
        for i, v in enumerate(Stock.stock_name):
            stock = Stock(name=v)
            Stock.stocks.append(stock)

    def stock_index(stock_name):
        """Takes stock name and returns the associated stock index"""
        if stock_name in Stock.stock_name:
            return Stock.stock_name.index(stock_name)
        else:
            return "Unknown stock"

    def increase_value(stock, amount):
        """Called from Dice.roll(), handles increasing value of selected stock"""

        def double_stock(stock):
            """Called from Stock.increase_value(), handles doubling player held stock quantity"""
            Stock.stocks[stock].value = 100
            # Check all players to see who is holding shares of stock
            # if player has any shares, double amount
            print(Stock.stocks[stock].value)

        stock_index = Stock.stock_name.index(stock)       
        Stock.stocks[stock_index].value = Stock.stocks[stock_index].value + amount
        if Stock.stocks[stock_index].value > 195:
            double_stock(stock)

    def decrease_value(stock, amount):
        """Called from Dice.roll(), handles subtracting from stock value"""

        def split_stock(stock):
            """Called from Stock.decrease_value(), handles removing all of selected stock from player inventory"""
            Stock.stocks[stock].value = 100
            # Check all players to see who is holding shares of stock_name (for i in range(0, total_players): player.player[i].stocks[*stock_index*] = 0)
            print(Stock.stocks[stock].value)

        stock_index = Stock.stock_name.index(stock)
        Stock.stocks[stock_index].value = Stock.stocks[stock_index].value - amount
        print(Stock.stocks[stock_index].value)
        if Stock.stocks[stock_index].value < 5:
            split_stock(stock)

class Dice:
    "Dice properties"

    action = ["Up", "Down", "Dividend"]
    amount = [5, 10, 20]

    def roll():
        """Rolls 3 dice (Stock.stock_name, Dice.action, Dice.amount) and prints the results to the screen."""
        stock = random.choice(Stock.stock_name)
        action = random.choice(Dice.action)
        amount = random.choice(Dice.amount)
        print(stock, action, amount)

        #Make appropriate changes to stock based on roll
        if action == Dice.action[0]:
            Stock.increase_value(stock, amount)
        elif action == Dice.action [1]:
            Stock.decrease_value(stock, amount)
        else:
            Player.dividend(stock, amount)

class Menu:
    "All menu screens"
    stocks = Stock.stock_name #Answer for stock name
    action = ["Buy", "Sell", "Done", ""]
    amount = [range(1-1000)]
    num_player = range(1, 8)
    menu = [range(1, 3)]
    name = "name"

    def main_menu():
        """Displays start screen with options including: New Game, About, Exit"""
        print("""
            Stock Ticker
            ------------

            1. New Game
            2. About
            3. Exit

            """)
        choice = Menu.ask_question("Please select an option: 1, 2 or 3.\n", Menu.menu)
        if choice == "1":
            Menu.init_game()
        elif choice == "2":
            Menu.about_page()
        else:
            #Exit script
            pass

    def init_game():
        """Begins a new game where users can choose number of players, rounds, and player names."""
        Stock.create_stocks()
        #Ask which option they wish: 1. bot simulation, 2. bots and humans, 3.humans only
        choice = Menu.player_type()
        if choice == "1":
            num_bots = Player.create_bots()
        elif choice == "2":
            num_bots = Player.create_bots()
            num_humans = Player.create_humans()
        else:
            num_humans = Player.create_humans()
        num_players = Player.name_player(num_bots, num_humans)
        #Let players buy there initial stocks before rolling, 
        #but only move to next player when all money is gone 
        #or user chooses to end turn
        for i in range(0, num_players):
            Menu.player_info(i)
            Menu.stock_info()
            Player.buy_stock(i)
        #Choose number of rounds to play

    def main_game():
        """main gameplay loop"""
        pass

    def end_game():
        """Runs end of game final score, with winner and loser."""
        pass

    def about_page():
        """Displays About page, option 2 from main_menu()"""
        print("About page")
        back = Menu.ask_question("Press enter to go back.")
        Menu.main_menu()

    def player_type():
        """Choose between bots only, bots and humans, or just humans."""
        #1. bot simulation, 2. bots and humans, 3.humans only
        print("""
            Pick Game Mode
            --------------

            1. Bot Simulation
            2. Bots & Humans
            3. Humans Only

            """)
        choice = Menu.ask_question("Please select an option: 1, 2 or 3.\n", Menu.menu)
        return choice

    def set_rounds():
        """User chooses number of rounds to be played"""
        rounds = Menu.ask_question("How many rounds would you like to play? 1 - 1000 \n", Menu.amount)
        return int(rounds)

    def player_info(player):
        """Displays current players stats"""
        print(f"{Player.players[player].name}'s Stats:")
        print(f"Money{str(Player.players[player].money).rjust(10, '-')}")
        for key in Player.players[player].stocks:
            value = Player.players[player].stocks[key]
            print(f"{str(key).ljust(10, '-')}-{value}")

    def stock_info():
        """Displays current stock prices"""
        print("Stock Prices:")
        for i, v in enumerate(Stock.stock_name):
            print(f"{str(Stock.stocks[i].name).ljust(10,'-')}-{Stock.stocks[i].value}")

    def ask_question(question, answers):
        """test = ask_question("What question?", ["y","n"])"""
        asking = True
        while asking:
            response = input(f"{question}")
            if answers == Menu.name:
                return response
            elif response not in answers:
                asking = False
            else:
                asking = False
        return response
        
Menu.main_menu()

#CHANGE: list comprehension for any empty lists using standard for loops
#ADD: Stock.double_stock()
#ADD: Stock.split_stock()
#FIX: Menu.init_game()
