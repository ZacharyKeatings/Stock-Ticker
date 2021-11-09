import random
import platform
import os
 
#Clears screen to make it easier to follow.
def clearScreen(user_os):
    if user_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    
#Starting message displayed at beginning of game
def welcomeMsg():
    welcome = """
                     STOCK TICKER
 
    The object of the game is to buy and sell stocks,
    and by doing so, accumulate a greater amount of
    money than the other players by the end of the game.
    """
    print(welcome)
 
# Choose how many players are in game as well as choose names
def createPlayers(player):
    ask = True
    while ask is True:
        num_players = input("Please choose between 2 and 8 players.\n")
        ask = False if num_players.isdigit() and 2 <= int(num_players) <= 8 else True
    for _ in range(int(num_players)):
        players.append(player_stats.copy())
    while player < len(players):
        players[player]["Name"] = input(f"What is player {player+1}'s name?\n")
        if players[player]["Name"] == "":
            print("Name cannot be left blank")
        else:
            player += 1
 
#Players can choose how many rounds game lasts
def chooseRounds():
    ask = True
    print("\nHow many rounds would you like to play?")
    while ask is True:
        rounds = input("Please choose a number between 1 - 100\n")
        ask = False if rounds.isdigit() and 1 <= int(rounds) <= 100 else True
    return int(rounds)
 
# Function to select random dice roll
def rollDice():
    stock = random.choice([0, 1, 2, 3, 4, 5]) # Relates to global stock_value and stock_list variable index
    action = random.choice(["Up", "Down", "Dividend"])
    amount = random.choice([5, 10, 20])
 
    stockChange(stock, action, amount, player, num_players)
    print("----------")
    print(stock_list[stock], action, amount)
    print("----------\n")
 
# Takes results of rollDice() and applies it to the Stock value
def stockChange(stock, action, amount, player, num_players):
    if action == "Up":
        stock_value[int(stock)] = stock_value[int(stock)] + amount
        if stock_value[int(stock)] >= 200:
            while player < num_players:
                if players[player][str(stock)] == 0:
                    player += 1
                elif players[player][str(stock)] > 0:
                    oldValue = players[player][str(stock)]
                    players[player][str(stock)] = players[player][str(stock)] * 2
                    newValue = players[player][str(stock)]
                    print(f"""{players[player]["Name"]} just doubled their {stock_list[stock]} stock from {oldValue} to {newValue}""")
                    player += 1
            stock_value[int(stock)] = 100
    elif action == "Down":
        stock_value[int(stock)] = stock_value[int(stock)] - amount
        if stock_value[int(stock)] <= 0:
            while player < num_players:
                if players[player][str(stock)] == 0:
                    player += 1
                elif players[player][str(stock)] > 0:
                    players[player][str(stock)] = players[player][str(stock)] * 0
                    newValue = players[player][str(stock)] * 0
                    print(f"""{players[player]["Name"]} got unlucky and lost all of their {stock_list[stock]} stock""")
                    player += 1
            stock_value[int(stock)] = 100
    elif action == "Dividend":
        if stock_value[int(stock)] >= 100:
            while player < num_players:
                if players[player][str(stock)] == 0:
                    player += 1
                elif players[player][str(stock)] > 0:
                    players[player]["Money"] += (stock_value[int(stock)] * int(amount))
                    newValue = stock_value[int(stock)] * int(amount)
                    print(f"""\n{players[player]["Name"]} just got ${newValue} from {stock_list[stock]}\n""")
                    player += 1
    return stock_value[stock]

#Displays the current players stats such as money, and owned stocks
def curPlayerInfo(player):
    print(f"""----------It is {players[player]["Name"]}'s turn----------\n""")
    print(f"""Money:      {players[player]["Money"]}""")
    print(f"""{stock_list[0]}:       {players[player]["0"]}""")
    print(f"""{stock_list[1]}:     {players[player]["1"]}""")
    print(f"""{stock_list[2]}:        {players[player]["2"]}""")
    print(f"""{stock_list[3]}:      {players[player]["3"]}""")
    print(f"""{stock_list[4]}:      {players[player]["4"]}""")
    print(f"""{stock_list[5]}: {players[player]["5"]}\n""")
 
#Controls stock purchasing functionality
def playerBuy(player):
    if int(int(players[player]["Money"])) < int(can_buy):
        clearScreen(user_os)
        print("You can't afford any stocks.\n")
    else:
        stock_buy = input("Which stock would you like to buy?\n")
        stock_buy = stock_buy.capitalize()
        if stock_buy not in stock_list:
            clearScreen(user_os)
            print("Please choose a valid stock.\n")
        else:
            ask = True
            while ask is True:
                buy_number = input(f"How many shares of {stock_buy} would you like to buy?\n")
                ask = False if buy_number.isdigit() else True
            if int(players[player]["Money"]) < (stock_value[stock_list.index(stock_buy)] * int(buy_number)):
                clearScreen(user_os)
                print(f"You can't afford {buy_number} stock(s) of {stock_buy}.\n")
            elif int(players[player]["Money"]) >= (stock_value[stock_list.index(stock_buy)] * int(buy_number)):
                players[player]["Money"] = players[player]["Money"] - int(stock_value[stock_list.index(stock_buy)] * int(buy_number))
                players[player][str(stock_list.index(stock_buy))] += int(buy_number)
                clearScreen(user_os)
                print(f"You bought {buy_number} {stock_buy} stock(s).\n")
 
#Controls stock selling functionality
def playerSell(player):
    stock_sell = input("Which stock would you like to sell?\n")
    stock_sell = stock_sell.capitalize()
    if stock_sell not in stock_list:
        clearScreen(user_os)
        print("Please choose a valid stock.\n")
    else:
        ask = True
        while ask is True:
            number_sell = input(f"How many shares of {stock_sell} would you like to sell?\n")
            ask = False if number_sell.isdigit() else True
        if int(players[player][str(stock_list.index(stock_sell))]) < int(number_sell):
            clearScreen(user_os)
            print("You don't have that much.\n")
        elif int(players[player][str(stock_list.index(stock_sell))]) >= int(number_sell):
            players[player]["Money"] = players[player]["Money"] + int(stock_value[stock_list.index(stock_sell)] * int(number_sell))
            players[player][str(stock_list.index(stock_sell))] -= int(number_sell)
            clearScreen(user_os)
            print(f"You sold {number_sell} {stock_sell} stock(s).\n")
 
#Players can purchase stocks before game begins
def firstPurchase(player, num_players):    
    while player < num_players:
        print("""
            STOCK TICKER
    """)
        print("""
    Before the game starts, each player gets the
    choice of purchasing any stocks they want.
        """)
        curPlayerInfo(player)
        currentPrices()
        user_choice = input(f"{choices[0]}, {choices[1]} or {choices[2]}?\n")
        user_choice = user_choice.capitalize()
        if user_choice not in choices:
            clearScreen(user_os)
            print("Please choose a correct action.\n")
        if user_choice == choices[2] or user_choice == choices[3]:
            clearScreen(user_os)
            player += 1
        elif user_choice == choices[0]:
            playerBuy(player)
        elif user_choice == choices[1]:
            playerSell(player)
    clearScreen(user_os)
    print("         \nThe game has begun!\n")
    rollDice()
 
#Displays current price based on results of rollDice()
#Add justification to keep stats evenly space for any stock name
def currentPrices():
    print("Stock Prices:")
    print("-----")
    print(f"{stock_list[0]}:       {stock_value[0]}")
    print(f"{stock_list[1]}:     {stock_value[1]}")
    print(f"{stock_list[2]}:        {stock_value[2]}")
    print(f"{stock_list[3]}:      {stock_value[3]}")
    print(f"{stock_list[4]}:      {stock_value[4]}")
    print(f"{stock_list[5]}: {stock_value[5]}")
    print("-----")
    print("")

#Main gameplay mechanics
def mainGame(player, rounds, num_players, max_rounds):
    while rounds < max_rounds:
        if player < num_players:
            print(f"Round: {rounds+1}/{max_rounds}\n")
            curPlayerInfo(player)
            currentPrices()
            user_choice = input(f"{choices[0]}, {choices[1]} or {choices[2]}?\n")
            user_choice = user_choice.capitalize()
            if user_choice not in choices:
                clearScreen(user_os)
                print("Please choose a correct action.\n")
            if user_choice == choices[2] or user_choice == choices[3]:
                player += 1
                clearScreen(user_os)
                if rounds+1 == max_rounds and player == num_players:
                    player = 0
                    endGame(player, num_players)
                else:
                    rollDice()
            elif user_choice == choices[0]:
                playerBuy(player)
            elif user_choice == choices[1]:
                playerSell(player)
        elif player == num_players:
            player = 0
            rounds += 1
 
#When result of chooseRounds() is met, game sells any held stocks at current market value and displays all players total money
def endGame(player, num_players):
    while player < num_players:
        stock_number = 0
        num_stocks = len(stock_value)
        while stock_number < num_stocks:
            players[player]["Money"] += players[player][str(stock_number)] * stock_value[stock_number]
            stock_number += 1
        print(f"""{players[player]["Name"]} has ${players[player]["Money"]}""")
        player += 1
        stock_number = 0
    input("Press ENTER to exit")
    exit()
    
####################
# Global Variables #
####################
stock_list = ["Gold", "Silver", "Oil", "Bonds", "Grain", "Industrial"]
stock_value = [100, 100, 100, 100, 100, 100]
choices = ["Buy", "Sell", "Done", ""]
player_stats = {'Name': 'None', 'Money': 5000, '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
players = []
can_buy = min(stock_value)
user_os = platform.system()
player = 0
rounds = 0

####################
#    Begin game    #
####################
welcomeMsg()
createPlayers(player)
num_players = len(players)
max_round = chooseRounds()
max_rounds = int(max_round)
clearScreen(user_os)
firstPurchase(player, num_players)
mainGame(player, rounds, num_players, max_rounds)
