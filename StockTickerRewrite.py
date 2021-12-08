import random
import math

class Player:
    "Player stats"

    players = []

    def __init__(self, name = "", money = 5000):
        """stocks refer to quantity of given stock. money is available money. name is chosen by user"""
        self.name = name
        self.money = money
        #Change stocks names here and in Stock class
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
        return num_humans

    def name_player(num_players):
        """Creates names for all bot + human players"""
        for num in range(1, num_players+1):
            player = Player(Menu.ask_question(f"What is Player {num}'s name?\n", Menu.name))
            print(f"Player {num} is now named: {player.name}")
            Player.players.append(player)

    def current_prices(player):
        """Checks if player can afford any stocks."""
        current_prices = []
        for num in range(0, 6):
            stock_price = Stock.stocks[num].value
            current_prices.append(stock_price)
        if Player.players[player].money < min(current_prices):
            return False
        else:
            return True

    def max_purchase(stock_name, current_player):
        """Defines the highest quantity of selected stock user can purchase with current funds"""
        index = Stock.stock_index(stock_name)
        max_purchase = math.trunc(Player.players[current_player].money/Stock.stocks[index].value)
        return max_purchase

    def buy_stock(current_player):
        """User chooses which stock to buy and the quantity"""
        if Player.current_prices(current_player) is False:
            print("You can't afford any stocks")
        else:        
            buy_name = Menu.ask_question("Which stock would you like to buy?\n", Menu.stocks).capitalize()
            print(f"You can buy {Player.max_purchase(buy_name, current_player)} share(s) of {buy_name}.")
            while int(Player.max_purchase(buy_name, current_player)) >= 1:
                buy_number = int(Menu.ask_question("How many shares do you wish to purchase?", range(0,Player.max_purchase(buy_name, current_player))))
                Player.players[current_player].money -= (buy_number * Stock.stocks[Stock.stock_index(buy_name)].value)
                Player.players[current_player].stocks[buy_name] += buy_number
                Menu.stat_screen(current_player)            

    def sell_stock(current_player):
        """User choose which stock to sell and the quantity"""
        can_sell = []
        for key in Player.players[current_player].stocks:
            value = Player.players[current_player].stocks[key]
            if value > 0:
                can_sell.append(value)
        if can_sell is False:
            print("You don't have any stocks to sell!")
        else:
            sell_name = Menu.ask_question("Which stock would you like to sell?", can_sell).capitalize()
            sell_index = Stock.stock_name.index(sell_name)
            max_sell = Player.players[current_player].stocks[sell_name]
            sell_amount = Menu.ask_question(f"How many shares of {sell_name} do you want to sell?", range(0, max_sell))
            sell_amount = int(sell_amount)
            Player.players[current_player].money += sell_amount * Stock.stocks[sell_index].value
            Player.players[current_player].stocks[sell_name] -= sell_amount

    def dividend(stock, div_roll):
        """Called from Dice.roll(), handles issuing players holding selected stock bonus funds"""
        stock_index = Stock.stock_index(stock)
        dividend = (div_roll / 100) + 1
        print(f"{dividend=}{div_roll=}")
        if Stock.stocks[stock_index].value >= 100:
            print(f"{stock} will pay out {div_roll}%.")
            for i, v in enumerate(Player.players):
                bonus = Player.players[i].stocks[stock] * dividend
                Player.players[i].money = Player.players[i].money + bonus
                Player.players[i].money = int(Player.players[i].money)
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

    #Change stock names here and Player class
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
        stock_index = Stock.stock_name.index(stock)       
        Stock.stocks[stock_index].value = Stock.stocks[stock_index].value + amount
        if Stock.stocks[stock_index].value > 195:
            Stock.double_stock(stock)

    def double_stock(stock):
        """Handles doubling player held stock quantity if stock value goes above 195"""
        Stock.stocks[stock].value = 100
        for i, v in enumerate(Player.players):
            Player.players[i].stocks[stock] = Player.players[i].stocks[stock] * 2

    def decrease_value(stock, amount):
        """Called from Dice.roll(), handles subtracting from stock value"""
        stock_index = Stock.stock_name.index(stock)
        Stock.stocks[stock_index].value = Stock.stocks[stock_index].value - int(amount)
        if Stock.stocks[stock_index].value < 5:
            Stock.split_stock(stock)

    def split_stock(stock):
        """Called from Stock.decrease_value(), handles removing all of selected stock from player inventory"""
        Stock.stocks[stock].value = 100
        for i, v in enumerate(Player.players):
            Player.players[i].stocks[stock] = 0

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

        if action == Dice.action[0]:
            Stock.increase_value(stock, amount)
        elif action == Dice.action [1]:
            Stock.decrease_value(stock, amount)
        else:
            Player.dividend(stock, amount)

class Menu:
    "All menu screens"

    #These are all various answers to ask_question()
    stocks = Stock.stock_name
    action = ["Buy", "Sell", "Pass", ""]
    amount = [range(1-1000)]
    num_player = range(1, 8)
    menu = [range(1, 3)]
    name = "name"

    #Initiating main variables
    rounds = 0
    num_players = 0

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
            Menu.setup_game()
        elif choice == "2":
            Menu.about_page()
        else:
            #Exit script
            pass

    def setup_game():
        """Begins a new game where users can choose number of players, rounds, and player names."""
        #Display
        print("""
            Setup New Game
            --------------

            """)
        
        #Populate Stock.stocks list with stock data
        Stock.create_stocks()

        #Choose between bots, bots/humans, humans, count total players
        Menu.num_players = Menu.player_type()

        #Name all players
        Player.name_player(Menu.num_players)

        #set number of rounds to be played in current game
        Menu.set_rounds()

        #Let players buy there initial stocks before rolling, 
        #but only move to next player when all money is gone 
        #or user chooses to end turn
        v = 0
        while v < Menu.num_players:
            for i in range(0, Menu.num_players):
                Menu.stat_screen(i)
                v += 1
        #Run the main game now:
        Menu.main_game()


    def main_game():
        """main gameplay loop"""
        #run main block however many rounds user chose
        current_round = 1
        while current_round <= int(Menu.rounds):
            #loop through players constantly
            for i in range(0, Menu.num_players):
                #Display current round out of total rounds
                print(f"{current_round}/{Menu.rounds}")
                #Dice roll
                Dice.roll()
                #stat screen
                Menu.stat_screen(i)
                #buy, sell or pass
                input("Press enter to continue.\n")

            #After all players get a turn in the round, increase round count
            current_round += 1

        #End of final round, run end_game
        Menu.end_game()
        

    def end_game():
        """Runs end of game final score, with winner and loser."""
        #Loops through each player
        for i in range(0, Menu.num_players):
            #Loops through each stock in i player
            for s in enumerate(Stock.stock_name):
                Player.players[i].money += Player.players[i].stocks[s] * Stock.stocks[s].value

        #Print out all players final score
        for p in enumerate(Menu.num_players):
            print(f"{Player.players[p].money=}")

        #rank most money to least money
        

    def about_page():
        """Displays About page, option 2 from main_menu()"""
        print("""
            About Stock Ticker
            ------------------

            The object of the game is 
            to buy and sell stocks, and 
            by so doing accumulate a 
            greater amount of money 
            than the other players.

            """)
        Menu.ask_question("Press enter to go back.", Menu.action[3])
        Menu.main_menu()

    def player_type():
        """Choose between bots only, bots and humans, or just humans."""
        print("""
            Pick Game Mode
            --------------

            1. Bot Simulation
            2. Bots & Humans
            3. Humans Only

            """)
        choice = Menu.ask_question("Please select an option: 1, 2 or 3.\n", Menu.menu)
        if choice == "1":
            num_players = Player.create_bots()
            return int(num_players)
        elif choice == "2":
            num_bots = Player.create_bots()
            num_humans = Player.create_humans()
            num_players = int(num_bots) + int(num_humans)
            return num_players
        else:
            num_humans = Player.create_humans()
            return int(num_humans)

    def set_rounds():
        """User chooses number of rounds to be played"""
        rounds = Menu.ask_question("How many rounds would you like to play? 1 - 1000 \n", Menu.amount)
        Menu.rounds = rounds

    def stat_screen(current_player):
        Menu.player_info(current_player)
        Menu.stock_info()
        Player.buy_stock(current_player)

    def player_info(player):
        """Displays current players stats"""
        print(f"{Player.players[player].name}'s Stats:")
        print("Money-".ljust(11, '-') + str(Player.players[player].money))
        for key in Player.players[player].stocks:
            value = Player.players[player].stocks[key]
            print(f"{str(key).ljust(11, '-')}{value}")

    def stock_info():
        """Displays current stock prices"""
        print("Stock Prices:")
        for i, v in enumerate(Stock.stock_name):
            print(f"{str(Stock.stocks[i].name).ljust(11,'-')}{Stock.stocks[i].value}")

    def game_choices(current_player):
        """Gives user option to buy, sell or pass"""
        choice = Menu.ask_question("Would you like to buy, sell, or pass?", Menu.choice)
        if choice == Menu.choice[0]:
            Player.buy_stock(current_player)
        elif choice == Menu.choice[1]:
            Player.sell_stock(current_player)
        else:
            pass

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

# CHANGE: List comprehension for any empty lists using standard for loops?
# ADD: Simple bot AI: 3 difficulties - low, moderate, and high risk.
#     Various risks buy and sell at different rates and values
#     Ex: - High risk buys near 180 or 20
#         - Moderate risk buys near 180, but sells near 20
#         - Low risk buys low, but not below 25, sells near 20
# ADD: Proper looping in Menu.setup_game() so at end of method, it runs Menu.main_game()
# CONSIDER: keep bots in player class, or create separate class?
# ADD: Bot.buy_stock()
# ADD: Bot.sell_stock()
# FIX: Menu.end_game() - line 284, in end_game
#                        Player.players[i].money += Player.players[i].stocks[s] * Stock.stocks[s].value
#                        KeyError: (0, 'Gold')
