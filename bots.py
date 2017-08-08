class Bot:
    """Base class for all bots. Creates bot memory and common functions. """

    nos_opponent = 0    # Tracks the total number of opponents in the tournament
    nos_rounds = 0      # Tracks the total number of rounds in a 2 way fight
    bottypelist = []
    botlist = []

    def __init__(self, name):
        self.name = name            # Name of the bot
        self.memory_own = []        # Memory of own choices
        self.memory_opponent = []   # Memory of opponent's choices. TODO: Correct data structure for multiple opponents?


class BotCopycat(Bot):
    def strategy(self):
        # Bot's strategy goes here
        if len(self.memory_opponent) == 0:
            return True                         # Always starts by cooperating first.
        else:
            return self.memory_opponent[-1]     # Returns the last known choice made by the opponent


class BotSaint(Bot):
    def strategy(self):
        return True                             # Always cooperates


class BotCheat(Bot):
    def strategy(self):
        return False                            # Always cheats


class BotGrudger(Bot):
    def __init__(self, name):
        self.name = name                        # Name of the bot
        self.memory_own = []                    # Memory of own choices
        self.memory_opponent = []               # Memory of opponent's choices. TODO: Correct data structure for multiple opponents?
        self.grudge_activated = False           # Not grudging to begin with

    def strategy(self):

        if len(self.memory_opponent) != 0 and self.memory_opponent[-1] == False:
            self.grudge_activated = True  # Activated grudge since opponent's previous move was to cheat

        if self.grudge_activated == True:
            return False  # Bot has begun grudging
        else:
            return True


class BotUser(Bot):
    # This bot is the user playing against the existing algorithmic bots, by asking for user input
    def strategy(self):
        user_input = input('Do you wish to cheat or cooperate? Type 1 for cooperate, Type 0 for cheat:')
        if user_input == 1:
            return True
        else:
            return False
