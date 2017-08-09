import bots

# Ask user for number of bots in the competition

# Assign to bot.nos_opponent


# Need a list for types of bots



# Change this approach to initializing a list of bots using a list comprehension
# Todo: For multibot competition, they need to play each other pair wise.
# Todo: Results of multibot competition need to be visualized well. Use 'import bokeh'?

results = []
bot1_choices = []
bot2_choices = []
bot1_gain = []
bot2_gain = []

def outcome(choice1, choice2):
    # This function returns the payoffs, give the choices made by the bots.
    # Todo: the payoff should be an attribute of the tournament class?
    if choice1==True and choice2==True:
        return 2, 2
    if choice1==False and choice2==False:
        return 0, 0
    if choice1==True and choice2==False:
        return 3, -1
    if choice1==False and choice2==True:
        return -1, 3

def fight(bot1, bot2, nos_rounds):
    for i in range(nos_rounds):
        # Bot choices are recorded
        bot1_choices[i] = bot1.strategy()
        bot2_choices[i] = bot2.strategy()

        # Record gain in coins for each bot
        bot1_gain[i], bot1_gain[i] = outcome(bot1_choices[i], bot2_choices[i])

        # Add each bot's choices to its own and the other bot's memory, to allow for learning strategies
        bot1.memory_own.append(bot1_choices[i])
        bot2.memory_own.append(bot2_choices[i])
        bot1.memory_opponent.append(bot2_choices[i])
        bot2.memory_opponent.append(bot1_choices[i])

    print ('Fight complete!')
    bot1.score = sum(bot1_gain)
    bot2.score = sum(bot2_gain)
    if bot1.score > bot2.score:
        print(bot1.name, ' won!')
    elif bot2.score > bot1.score:
        print(bot2.name, ' won!')
    else:
        print('It\'s a tie!')
    return True

