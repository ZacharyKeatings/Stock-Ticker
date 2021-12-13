import operator
import random
import time
import math
import os

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

    def create_bots(player_type):
        """Creates user selected number of bots (1 - 8)"""
        Menu.clear_console()
        if player_type == 1:
            num_bots = int(Menu.ask_question("""
            Choose Number Of Bots
            ---------------------

            Please choose the number 
            of bots you would like 
            to include in this 
            simulation between 2 - 8.

            """, Menu.num_player))
            return num_bots
        elif player_type == 2:
            num_bots = int(Menu.ask_question(f"""
            Choose Number Of Bots
            ---------------------

            Please choose the number 
            of bots you would like to 
            include in this simulation 
            between {min(Menu.num_bot)} - {max(Menu.num_bot)}.

            """, Menu.num_bot))
            return num_bots

    def create_humans(player_type):
        """Creates user chosen number of human players (2 to 8)"""
        Menu.clear_console()
        if player_type == 2:
            num_humans = int(Menu.ask_question(f"""
            Choose Number Of People
            -----------------------

            Please choose the number 
            of people you would like 
            to include between 1 - {8 - Menu.num_bots}.

            """, Menu.numhumans_response))
            return num_humans
        elif player_type == 3:
            num_humans = int(Menu.ask_question(f"""
            Choose Number Of People
            -----------------------

            Please choose the number 
            of people you would like 
            to include between {min(Menu.num_human)} - {max(Menu.num_human)}
            """, Menu.num_human))
            return num_humans

    def name_bots(num_bots):
        Menu.clear_console()
        for bots in range(1, Menu.num_bots+1):
            name = Menu.ask_question(f"What is Bot #{bots}'s name?\n", Menu.name) + " The Bot"
            player = Bot()
            print(f"Bot #{bots} is now named: {name}.")
            Player.players.append(player)
            Player.players[bots-1].name = name

    def name_humans(num_humans):
        Menu.clear_console()
        for human in range(1, Menu.num_humans+1):
            player = Player(Menu.ask_question(f"What is Player {human}'s name?\n", Menu.name))
            print(f"Player {human} is now named: {player.name}")
            Player.players.append(player)

    def can_buy(current_player):
        """Checks if player can afford any stocks."""
        current_prices = []
        for num in range(0, 6):
            stock_price = Stock.stocks[num].value
            current_prices.append(stock_price)
        if Player.players[current_player].money < min(current_prices):
            print()
            return False
        else:
            return True

    def max_purchase(stock_name, current_player):
        """Defines the highest quantity of selected stock user can purchase with current funds"""
        max_purchase = math.trunc(int(Player.players[current_player].money) / Stock.stocks[Stock.stock_index(stock_name.capitalize())].value)
        return max_purchase

    def buy_stock(current_player):
        """User chooses which stock to buy and the quantity"""
        buy_name = Menu.ask_question("Which stock would you like to buy?\n", Menu.stocks)
        print(f"You can buy {Player.max_purchase(buy_name, current_player)} share(s) of {buy_name}.")
        buy_number = int(Menu.ask_question("How many shares do you wish to buy?\n", range(0,Player.max_purchase(buy_name, current_player))))
        Player.players[current_player].money -= (buy_number * Stock.stocks[Stock.stock_index(buy_name.capitalize())].value)
        Player.players[current_player].stocks[buy_name.capitalize()] += buy_number

    def can_sell(current_player):
        """Checks if the current player has any stocks to sell."""
        can_sell = []
        for key in Player.players[current_player].stocks:
            value = Player.players[current_player].stocks[key]
            if value > 0:
                can_sell.append(key)
        
        if can_sell == []:
            return False
        else:
            return can_sell

    def sell_stock(current_player):
        """User choose which stock to sell and the quantity"""
        sell_name = Menu.ask_question("Which stock would you like to sell?\n", Player.can_sell(current_player))
        #!replace stock_index object with stock_index function
        sell_index = Stock.stock_name.index(sell_name.capitalize())
        max_sell = Player.players[current_player].stocks[sell_name.capitalize()]
        sell_amount = int(Menu.ask_question(f"How many shares of {sell_name.capitalize()} do you want to sell?\n", range(0, max_sell)))
        Player.players[current_player].money += sell_amount * Stock.stocks[sell_index].value
        Player.players[current_player].stocks[sell_name.capitalize()] -= sell_amount

    def dividend(stock, div_roll):
        """Called from Dice.roll(), handles issuing players holding selected stock bonus funds"""
        #!replace stock_index object with stock_index function
        stock_index = Stock.stock_index(stock)
        dividend = (div_roll / 100) + 1
        if Stock.stocks[stock_index].value >= 100:
            print(f"{stock} will pay out {div_roll}%.")
            for i, v in enumerate(Player.players):
                bonus = Player.players[i].stocks[stock] * dividend
                Player.players[i].money = Player.players[i].money + int(bonus)
                Player.players[i].money = int(Player.players[i].money)
                print(f"{Player.players[i].name} received ${int(bonus)}.")
        else:
            print(f"{stock} is under 100 and will not payout.")
            return None

class Bot(Player):
    "All actions for bots"

    buy_list = []
    sell_list = []

    def __init__(self, difficulty = 0):
        super().__init__(self)
        self.difficulty = difficulty

    def set_difficulty(current_bot):
        """This sets the difficulty level for a selected bot in the game."""
        Menu.clear_console()
        print("""
            Choose Bot Difficulty
            ---------------------

            1. Low risk:   -Buys: Any stock under 100, but above 30
                           -Sells: When held stocks hit 25 or below
            2. Medium risk -Buys: Prioritizes stocks valued at 180 or above
                           -Sells: When held stocks hit 25 or below
            3. High risk   -Buys: Prioritizes stocks valued near 180 and 20
                           -Sells: Holds all stocks

            """)
        choice = Menu.ask_question(f"Which difficulty level will {Player.players[current_bot].name} be set to?\n", Menu.menu)
        if choice == 1:
            Player.players[current_bot].difficulty = 1
        elif choice == 2:
            Player.players[current_bot].difficulty = 2
        else:
            Player.players[current_bot].difficulty = 3

    def bot_start(current_bot):
        """Runs in Menu.setup_game only"""
        for i in Stock.stock_name:
            Bot.buy_list.append(i)
        Bot.bot_buy(current_bot)

    def bot_turn(current_bot, current_round):
        """Handles full range of turn actions for human players."""
        playing = True
        Dice.roll()
        while playing:
            if Bot.can_buy(current_bot) is False and Bot.can_sell(current_bot) is False:
                Menu.stat_screen(current_bot, current_round)
                print("Please press enter to continue.")
                time.sleep(2)
                playing = False
            elif Bot.can_buy(current_bot) is False:
                Menu.stat_screen(current_bot, current_round)
                print("Would you like to Sell or Pass?")
                print("Sell")
                Bot.bot_sell(current_bot)
            elif Bot.can_sell(current_bot) is False:
                Menu.stat_screen(current_bot, current_round)
                print("Would you like to Buy or Pass?")
                print("Buy")
                Bot.bot_buy(current_bot)
            else:
                Menu.stat_screen(current_bot, current_round)
                print("Would you like to Buy, Sell, or Pass?")
                print("Sell")
                Bot.bot_sell(current_bot)

    def can_buy(current_bot):
        if Player.players[current_bot].difficulty == 1:
            Bot.low_risk(current_bot)
            bot_buy = Bot.buy_list
            if bool(bot_buy) is False:
                return False
            else:
                return True
        elif Player.players[current_bot].difficulty == 2:
            Bot.medium_risk(current_bot)
            bot_buy = Bot.buy_list
            if bool(bot_buy) is False:
                return False
            else:
                return True
        else:
            Bot.high_risk(current_bot)
            bot_buy = Bot.buy_list
            if bool(bot_buy) is False:
                return False
            else:
                return True

    def bot_buy(current_bot):
        """Bot buy stock method"""
        print("Which stock would you like to buy?")
        buy_name = random.choice(Bot.buy_list)
        print(buy_name)
        print(f"You can buy {Player.max_purchase(buy_name, current_bot)} share(s) of {buy_name}.")
        print("How many shares do you wish to buy?")
        #!either make bot buy max amount, or keep buying random amounts between 1 - max purchase
        buy_number = Player.max_purchase(buy_name, current_bot)
        print(buy_number)
        Player.players[current_bot].money -= (buy_number * Stock.stocks[Stock.stock_index(buy_name)].value)
        Player.players[current_bot].stocks[buy_name] += buy_number
        Bot.buy_list = []
        time.sleep(3)

    def can_sell(current_bot):
        if Player.players[current_bot].difficulty == 1:
            Bot.low_risk(current_bot)
            bot_sell = Bot.sell_list
            if bool(bot_sell) is False:
                return False
            else:
                return True
        elif Player.players[current_bot].difficulty == 2:
            Bot.medium_risk(current_bot)
            bot_sell = Bot.sell_list
            if bool(bot_sell) is False:
                return False
            else:
                return True
        else:
            return False

    def bot_sell(current_bot):
        """Low risk level sell stock method"""
        print("Which stock would you like to sell?")
        sell_name = random.choice(Bot.sell_list)
        print(sell_name)
        #!replace stock_index object with stock_index function
        sell_index = Stock.stock_name.index(sell_name)
        max_sell = Player.players[current_bot].stocks[sell_name]
        print(f"How many shares of {sell_name} do you want to sell?")
        print(max_sell)
        Player.players[current_bot].money += max_sell * Stock.stocks[sell_index].value
        Player.players[current_bot].stocks[sell_name] -= max_sell
        Bot.sell_list = []
        time.sleep(3)

    def low_risk(current_bot):
        """Difficulty level: 1."""
        for k, v in enumerate(Stock.stocks):
            if Stock.stocks[k].value > 95:
                Bot.buy_list.append(Stock.stocks[k].name)
            if Stock.stocks[k].value < 30:
                Bot.sell_list.append(Stock.stocks[k].name)

    def medium_risk(current_bot):
        """Difficulty level: 2."""
        for k, v in enumerate(Stock.stocks):
            if Stock.stocks[k].value > 175:
                Bot.buy_list.append(Stock.stocks[k].name)
            if Stock.stocks[k].value < 30:
                Bot.sell_list.append(Stock.stocks[k].name)

    def high_risk(current_bot):
        """Difficulty level: 3."""
        for k, v in enumerate(Stock.stocks):
            if Stock.stocks[k].value > 175:
                Bot.buy_list.append(Stock.stocks[k].name)
            if Stock.stocks[k].value < 25:
                Bot.buy_list.append(Stock.stocks[k].name)

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
        #!replace stock_index object with stock_index function
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
        #!replace stock_index object with stock_index function
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

    #Initiating main variables
    rounds = 0
    num_bots = 0
    num_humans = 0
    num_players = 0

    #These are all various answers to ask_question()
    stocks = Stock.stock_name
    action = ["Buy", "Sell", "Pass", ""]
    amount = [i for i in range(1, 1001)]
    num_player = [i for i in range(1, 9)]
    num_bot = [i for i in range(1, 9)]
    num_human = [i for i in range(2, 9)]
    menu = [i for i in range(1, 4)]
    name = "name"
    numhumans_response = (8 - num_bots)

    def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def main_menu():
        """Displays start screen with options including: New Game, About, Exit"""
        print("""
            Stock Ticker
            ------------

            1. New Game
            2. About
            3. Exit

            """)
        choice = int(Menu.ask_question("Please select an option: 1, 2 or 3.\n", Menu.menu))
        if choice == 1:
            Menu.clear_console()
            Menu.setup_game()
        elif choice == 2:
            Menu.clear_console()
            Menu.about_page()
        else:
            exit()

    def setup_game():
        """Begins a new game where users can choose number of players, rounds, and player names."""
        
        #Populate Stock.stocks list with stock data
        Stock.create_stocks()

        #Choose between bots, bots/humans, humans, count total players
        Menu.player_type()
        Menu.num_players = Menu.num_bots + Menu.num_humans

        #Name bot and human players:
        #Only bots        
        if Menu.num_bots > 0 and Menu.num_humans == 0:
            Player.name_bots(Menu.num_bots)
        #Bots and humans
        elif Menu.num_bots > 0 and Menu.num_humans > 0:
            Player.name_bots(Menu.num_bots)
            Player.name_humans(Menu.num_players)
        #Only humans
        else:
            Player.name_humans(Menu.num_players)

        if Menu.num_bots > 0:
            for current_bot in range(Menu.num_bots):
                Bot.set_difficulty(current_bot)

        #set number of rounds to be played in current game
        Menu.set_rounds()

        #Let players buy there initial stocks before rolling, 
        #but only move to next player when all money is gone 
        #or user chooses to end turn
        for current_player in range(Menu.num_players):
            playing = True
            while playing:
                if current_player <= Menu.num_bots and Player.can_buy(current_player):
                    Menu.stat_screen(current_player)
                    Bot.bot_start(current_player)
                elif current_player > Menu.num_bots and Player.can_buy(current_player):
                    Menu.stat_screen(current_player)
                    Player.buy_stock(current_player)
                else:
                    Menu.clear_console()
                    playing = False

        #Run the main game now:
        Menu.clear_console()
        Menu.main_game()

    def main_game():
        """main gameplay loop"""
        current_round = 1
        while current_round <= int(Menu.rounds):
            for current_player in range(0, Menu.num_players):
                if current_player < Menu.num_bots:
                    Bot.bot_turn(current_player, current_round)
                Menu.human_turn(current_player, current_round)
            current_round += 1
            Menu.clear_console()
        Menu.end_game()
        
    def human_turn(current_player, current_round):
        """Handles full range of turn actions for human players."""
        playing = True
        Dice.roll()
        while playing:
            if Player.can_buy(current_player) is False and Player.can_sell(current_player) is False:
                Menu.stat_screen(current_player, current_round)
                choice = Menu.ask_question("Please press enter to continue.\n", Menu.action[3])
                playing = False
            elif Player.can_buy(current_player) is False:
                Menu.stat_screen(current_player, current_round)
                choice = Menu.ask_question("Would you like to Sell or Pass?\n", Menu.action)
                if choice.capitalize() == "Sell":
                    Player.sell_stock(current_player)
                else:
                    Menu.clear_console()
                    playing = False
            elif Player.can_sell(current_player) is False:
                Menu.stat_screen(current_player, current_round)
                choice = Menu.ask_question("Would you like to Buy or Pass?\n", Menu.action)
                if choice.capitalize() == "Buy":
                    Player.buy_stock(current_player)
                else:
                    Menu.clear_console()
                    playing = False
            else:
                Menu.stat_screen(current_player, current_round)
                choice = Menu.ask_question("Would you like to Buy, Sell, or Pass?\n", Menu.action)
                if choice.capitalize() == "Buy":
                    Player.buy_stock(current_player)
                elif choice.capitalize() == "Sell":
                    Player.sell_stock(current_player)
                else:
                    Menu.clear_console()
                    playing = False
                
    def end_game():
        """Runs end of game final score, with winner and loser."""
        #Loops through each player, adds stock value to money, displays total money
        ranking = {}
        for i, c in enumerate(Player.players):
            for k, n in enumerate(Stock.stock_name):
                Player.players[i].money += Player.players[i].stocks[n] * Stock.stocks[k].value
            money = Player.players[i].money
            name = Player.players[i].name
            player_value = {name : money}
            ranking.update(player_value)
        sorted_ranking = dict(sorted(ranking.items(), key=operator.itemgetter(1), reverse=True))

        print("Here is the final score for each player in descending order:")
        for i, c in enumerate(sorted_ranking):
            print(f"{i+1}. {c} has ${sorted_ranking[c]}")
        
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
        Menu.clear_console()
        Menu.main_menu()

    def player_type():
        """Choose between bots only, bots and humans, or just humans."""
        print("""
            Setup New Game
            --------------

            Pick Game Mode:
            1. Bot Simulation
            2. Bots & Humans
            3. Humans Only

            """)
        choice = int(Menu.ask_question(f"Please select an option: {min(Menu.menu)} - {max(Menu.menu)}\n", Menu.menu))
        if choice == 1:
            Menu.num_bots = Player.create_bots(1)
        elif choice == 2:
            Menu.num_bots = Player.create_bots(2)
            Menu.num_humans = Player.create_humans(2)
        else:
            Menu.num_humans = Player.create_humans(3)

    def set_rounds():
        """User chooses number of rounds to be played"""
        rounds = int(Menu.ask_question(f"How many rounds would you like to play? {min(Menu.amount)} - {max(Menu.amount)}\n", Menu.amount))
        Menu.rounds = rounds

    def stat_screen(current_player, current_round = False, dice_outcome = False):
        """Displays all viable information like play, stock, current round and dice roll."""
        if current_round == False and dice_outcome == False:
            Menu.player_info(current_player)
            Menu.stock_info()
        elif dice_outcome == False:
            print(f"{current_round}/{Menu.rounds}")
            Menu.player_info(current_player)
            Menu.stock_info()
        else:
            print(f"{current_round}/{Menu.rounds}")
            print(dice_outcome)
            Menu.player_info(current_player)
            Menu.stock_info()

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

    def ask_question(question, answers):
        """test = ask_question("What question?", ["y","n"])"""
        asking = True
        while asking:
            response = input(f"{question}")
            if response.isdigit():
                response = int(response)
                return response
            elif response.capitalize() in answers:
                asking = False
                return response
            elif answers == Menu.name:
                return response
            else:
                print("That's not a proper choice!")

Menu.main_menu()
