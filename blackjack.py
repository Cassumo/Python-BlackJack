from random import choice
from sys import exit
#%% LISTS & DICTIONARIES
club = {
        "ace clubs": 11,
        "two clubs": 2,
        "three clubs": 3,
        "four clubs": 4,
        "five clubs": 5,
        "six clubs": 6,
        "seven clubs": 7,
        "eight clubs": 8,
        "nine clubs": 9,
        "ten clubs": 10,
        "jack clubs": 10,
        "queen clubs": 10,
        "king clubs": 10
        }
spade = {
        "ace spades": 11,
        "two spades": 2,
        "three spades": 3,
        "four spades": 4,
        "five spades": 5,
        "six spades": 6,
        "seven spades": 7,
        "eight spades": 8,
        "nine spades": 9,
        "ten spades": 10,
        "jack spades": 10,
        "queen spades": 10,
        "king spades": 10
        }
heart = {
        "ace hearts": 11,
        "two hearts": 2,
        "three hearts": 3,
        "four hearts": 4,
        "five hearts": 5,
        "six hearts": 6,
        "seven hearts": 7,
        "eight hearts": 8,
        "nine hearts": 9,
        "ten hearts": 10,
        "jack hearts": 10,
        "queen hearts": 10,
        "king hearts": 10
        }
diamond = {
        "ace diamonds": 11,
        "two diamonds": 2,
        "three diamonds": 3,
        "four diamonds": 4,
        "five diamonds": 5,
        "six diamonds": 6,
        "seven diamonds": 7,
        "eight diamonds": 8,
        "nine diamonds": 9,
        "ten diamonds": 10,
        "jack diamonds": 10,
        "queen diamonds": 10,
        "king diamonds": 10
        }
rand = [1,2,3,4]#Used in choosing which suit is used
player = [] #Player int score
players = [] #Player cards as str
pc = [] #PC int score
pcs = []#PC cards as str
pchidden = []#PC Hidden card as str
#%%
def starthand():
    global player, pc, pchidden
    x = 0
    while x != 2:
        hit(1) # for player
        if x == 0:
            hit(2) # for pc
        if x == 1:
            hit(3) # for hidden pc
        x += 1
    return
#%%
def append(x,y,z): #x = whos card, y = what is the card (dic key) z = dic value
    if x == 1:
        players.append(y)
        player.append(z)
    if x == 2:
        pcs.append(y)
        pc.append(z)
    if x == 3:
        pchidden.append(y)
        pc.append(z)
#%%
def wincheck(x):
    global player, pc, pcs, pchidden
    if sum(player) == 21 and sum(pc) != 21:
        x+=1
    if sum(pc) == 21 and sum(player) != 21:
        x+=2
    if sum(pc) == 21 and sum(player) == 21:
        x+=3
    if x == 1:
        print("Player wins")
        return(69)
    if x == 2:
        print("\nDealer hand:\n" + str(pcs) + str(pchidden) + "\nTotal: " + str(sum(pc)))
        print ("PC Wins")
        return(69)
    if x == 3:
        print ("Stalemate")
        return(69)
    else:
        return(False)
    
#%%
def hit(y):
    global club, spade, heart, diamond, rand, players, pcs
    if not rand:
        print("Deck Empty")
        print(club,spade,heart,diamond)
        exit()
        return
    val = choice(rand)
    if val == 1:
        x = club
    if val == 2:
        x = spade
    if val == 3:
        x = heart
    if val == 4:
        x = diamond
    card = choice(list(x.keys()))
    cardvalue = x.get(card)
    x.pop(card)
    append(y,card,cardvalue)#y = who is hitting, card = str, value = int
    if not x:
        rand.remove(1)
        print(x + " Empty")
#%%
def handstring():
    global player, players, pcs
    print("\nPlayer hand:\n" + str(players) + "\nTotal: " + str(sum(player)))
    print("\nDealer hand:\n" + str(pcs) + "?")
#%%
def main():
    global club,spade,heart,diamond,rand,player,pc,players,pcs
    x = 0
    while x != 2:
        hit(1) # for player
        if x == 0:
            hit(2) # for pc
        if x == 1:
            hit(3) # for hidden pc
        x += 1
    handstring()
    x = "null"
    check = wincheck(0)
    if x == 69:
        exit()
    if check == False:
        while x == "null":
            deal = input("Hit or stand (h or s): ")
            if deal == "h":
                hit(1)#the 1 indicates the player is hitting
                if sum(player) > 21 and 11 in player: #checks if the ace puts sum over 21
                    player.remove(11)
                    player.append(1)
                if sum(player) > 21:
                    handstring()
                    print("\nBust!")
                    x = "bust"
                else:
                    handstring()
            if deal == "s":
                x = "stand"
                print("\nStand")
    if x != "bust":
        while sum(pc) < 17 or sum(pc) < sum(player):
            hit(2)#the 2 shows the pc is hitting
            print("\nDealer hand:\n" + str(pcs) + str(pchidden) + "\nTotal: " + str(sum(pc)))
            if sum(pc) > 21 and 11 in pc: #checks if the ace puts sum over 21
                pc.remove(11)
                pc.append(1)
            if sum(pc) > 21:
                print("\nDealer Bust!")
    if sum(pc) > sum(player) and sum(pc) <22:
        print("\nPC Wins!")
    if sum(player) > sum(pc) and sum(player) <22:
        print("\nYou Win!")
    if sum(player) == sum(pc):
        print("\nStalemate")
#%%
print("Blackjack")
menu = input("Begin? ")
if menu == ("y"):
    main()
if menu == ("loop"):
    while True:
        hit()
else:
    print("\nEND")