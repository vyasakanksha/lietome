import bots
import tournament

# Ask user to define the game: firstly, the number of players
bots.Bot.nos_opponent = int(input('Enter Number of players:'))
bots.Bot.nos_rounds = int(input('Enter Number of rounds:'))
print('Currently only 2 players allowed. Sorry!')   # This can be corrected later
bots.Bot.nos_opponent = 2


# Creates blank array of required size. Could have just used append instead
bots.Bot.bottypelist = [None for x in range(bots.Bot.nos_opponent)]


# Ask user to specify the type of each bot.
# Need to accept inputs more than 2, or allow specifying as number of bots of each type.
print('Bot Key: \n1: CopyCat \n2: Saint \n3: Cheat \n4: Grudger \n5: User')
bots.Bot.bottypelist[0] = int(input('Enter first bot type:'))
bots.Bot.bottypelist[1] = int(input('Enter second bot type:'))


# Create a list holding a bot object of the correct type. These bots will then play each other.
for i in bots.Bot.bottypelist:
    if i == 1:
        bots.Bot.botlist.append(bots.BotCopycat('CopyCat'))
    if i == 2:
        bots.Bot.botlist.append(bots.BotSaint('Saint'))
    if i == 3:
        bots.Bot.botlist.append(bots.BotCheat('Cheat'))
    if i == 4:
        bots.Bot.botlist.append(bots.BotGrudger('Grudger'))
    if i == 5:
        bots.Bot.botlist.append(bots.BotUser('User'))

temp = tournament.fight(bots.Bot.botlist[0], bots.Bot.botlist[1], bots.Bot.nos_rounds)

# Output/Result plots go here