"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame


class Cubey(Sprite):
    def __init__(self, position):

myapp = App()
myapp.run()

"""

def Init():
    name = input ("Please select a name: ")
    age = input (name + ", how old are you? ")
    age = int (age)
    g = 0
    while g == 0:
        if age < 6:
            age = input ("Even prodigies can't be that young. Please select again: ")
            age = int (age)
        elif age > 13 and age < 19: 
            age = input ("You're a child, not a teenager. Please select again: ")
            age = int (age)
        elif age >= 19:
            age = input ("You're a child, not an adult. Please select again: ")
            age = int (age)
        else:
            print ("That will do. Now, time to become yourself.")
            g = 1
    print (" ")
    print ("You will have 50 attribute points to spend on ten categories: ")
    namestat = ["Bravery", "Tenacity", "Wisdom", "Cleverness", "Wit", "Luck", "Manipulation", "Ambition", "Beauty", "Optimism"]
    for i in namestat:
        print (i)
    print (" ")
    num = 50
    list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list2 = ["Bravery is the ability to act in a situation. ", "Tenacity is the ability to withstand pain. ", "Wisdom is the ability to acquire and recall knowledge, as well as the knowledge of when to use it. ", "Cleverness is the ability to solve problems quickly. ", "Wit is the ability to make friends and be liked. ", "Luck is a natural gift not quite described. ", "Manipulation is the ability to change minds in ways less honorable. ", "Ambition is the drive to excel and go beyond. ", "Beauty is a natural appearance and charm. ", "Optimism is the ability to see the best in a bad situation. "]
    for x in range (0, 10):
        desc = list2[x]
        print (desc)
        namre = namestat[x]
        e = 0
        while e == 0:
            g = 0
            while g == 0:
                ent = input (namre + ", out of ten. ")
                ent = int(ent)
                if ent < 0 or ent > 10:
                    print ("Don't be a novelty. Between zero and ten, please. ")
                else: 
                    g = 1
            print (namre + " total: " + str(ent))
            num = num - ent
            if num < 0:
                print ("Oh dear, you don't have enough energy points for that! Please select again! ")
                print (" ")
                num = num + ent
            else:
                e = 1
        print ("Points left: " + str(num))
        list1[x] = ent
        print (" ")
    if num > 0:
        print ("You didn't plan very well, did you. That doesn't speak well for your intelligence... ")
        print ("Cleverness: 0")
        list1[3] = 0
        print (" ")
    mgc = [5, 7, 2]
    phys = [1, 5, 3]
    con = [6, 8, 2]
    hap = [9, 4, 7]
    lik = [4, 0, 6]
    lead = [7, 6, 4]
    hero = [0, 1, 5]
    spi = [2, 9, 8]
    intel = [3, 2, 9]
    beg = [8, 3, 0]
    att = ["Magic", "Physical Fitness", "Connections in High Places", "Happiness", "Likeability", "Leadership", "Heroicness", "Spirituality", "Intelligence", "Beguiling"]
    nums2 = [mgc, phys, con, hap, lik, lead, hero, spi, intel, beg]
    names = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print ("Now, we will determine secondary statistics. ")
    print ("Secondary statistics have real impact in the game. They are determined by your primary statistics you have just entered, and are out of thirty. ")
    print ("Don't worry, all primary statistics are used once for all above categories. They are all equal! ")
    print ("The average score is 12.5. Most of your scores will end up being close to this. It's not possible to be negative!")
    print (" ")
    for x in range (0, 10):
        attr = att[x]
        varlist = nums2[x]
        major = varlist[0]
        minor = varlist[1]
        neg = varlist[2]
        majname = namestat[major]
        minname = namestat[minor]
        negname = namestat[neg]
        lvl = list1[major] + list1[major] + list1[minor] - (list1[neg])/2
        if lvl < 0:
            lvl = 0
        print (attr + ": Two times " + majname + " plus " + minname + " minus one half " + negname)
        print (attr + ": " + str(lvl))
        values[x] = lvl
        namer = input("Type anything to continue. ")
        names[x] = namer
        print (" ")
    valuez = values[:]
    val2 = valuez.sort()
    return values
    """
    maxm = val2[9]
    sec = val2[8]
    valuec = values[:]
    locsec = valuec.index(sec)
    valuz = valuec [:]
    valuz.remove(sec)
    locmax = valuz.index(maxm) + 1
    maxstat = att[locmax]
    secstat = att[locsec]
    print ("Your dominant skill is " + maxstat + ", followed by " + secstat + ". These skills will serve you well in the future. ")
    i = input ("Now, let us begin! ")
    """

def Transition():
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    
def Desc(room):
    if room == 1:
        print ("Courtyard Proper")
        print ("You are standing outside a spindly northern tower with a stained glass door. Around you, "
        + "an endless sea of grass ripples in the wind. It is eerily green, almost neon in its brightness. " +
        "Aside from overgrown paths east and west through the tresses, there is nothing for miles. ")
    if room == 2:
        print ("Sasha's Courtyard")
        print ("You are standing in a flattened patch of grass known as Sasha's Courtyard. " +
        "Around you, the green grass extends almost to your head. A path winds east through the jade ocean towards " +
        "what looks like a tower.")
    if room == 3:
        print ("Small Ditch")
        print ("The path east leading to the small ditch you are standing in is overgrown with moss. There is a hole " +
        "in the northern cave wall. Even in here, the grass is eerily green. ")
    if room == 4:
        print ("Crystal Cave")
        print ("The passage takes you into a small cave adorned with rainbow crystals. Somehow, you think you "
        + "have seen this place before... An abandoned mineshaft slopes east into blackness. Nailed beside it, a sign. "
        + "ONLY FOR THE HEROIC")
    if room == 5:
        print ("Mineshaft")
        print ("As you walk along the rusted tracks, you get the increasing feeling that you're walking in a circle. "
        + "But then, a light ahead!")
    if room == 6:
        print ("Atrium")
        print ("You are standing in the dark castle room known as the atrium. The only light comes from the stained " +
        "glass window of the southern door. Stairways wind up and down into blackness. ")
    if room == 7:
        print ("Billiard Room")
        print ("What was once the billiard room is now grey and filled with light. Stairs wind down the stone walls into blackness. ")
    if room == 8:
        print ("Basement")
        print ("In here, it is so dark that you can't " + 
        "see your feet in front of you. Even though there are no windows, this room is distinctly drafty. ")
    if room == 9:
        print ("Southern Corridor")
        print ("Somehow, you have stumbled upon a hidden corridor! The floor is "
        + "distinctly earthy, and you fear that the loose dirt ceiling will collapse on your head at any minute.")
    if room == 10:
        print ("Erdgeschoss Grounds")
        print ("Stumbling out of the passage, the first thing that you see is the brilliant light. " +
        "A crystalline lake stretches before you, the mountains reflected in pristine detail in the water. The "
        "grassy tower seems a million miles away...")
    print (" ")

def MoveProc(move):
    j = 0
    while j == 0:
        if move == "n":
            dire = 0
            j = 1
        elif move == "e":
            dire = 1
            j = 1
        elif move == "s":
            dire = 2
            j = 1
        elif move == "w":
            dire = 3
            j = 1
        elif move == "u":
            dire = 4
            j = 1
        elif move == "d":
            dire = 5
            j = 1
        else: 
            print ("Incorrect format")
            move = input (": ")
    return dire

def Movement(room, dire):
    r1 = [6, 3, 0, 2, 0, 0]
    r2 = [0, 1, 0, 0, 0, 0]
    r3 = [4, 0, 0, 1, 0, 0]
    r4 = [0, 5, 3, 0, 0, 0]
    r5 = [0, 9, 0, 0, 0, 0]
    r6 = [0, 0, 1, 0, 7, 8]
    r7 = [0, 0, 0, 0, 0, 6]
    r8 = [0, 0, 9, 0, 6, 0]
    r9 = [0, 0, 10, 0, 0, 0]
    r10 = [0, 0, 0, 0, 0, 0]
    rlist = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
    rnum = room - 1
    roomlist = rlist[rnum]
    pos = roomlist[dire]
    if pos == 0:
        print ("You cannot go in that direction! ")
        return room, pos
    else:
        room = pos
        return room, pos
        
def inventory(room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10):
    ret = [rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10]
    lizt = ["small wooden key", "gilded envelope"]
    rnum = room
    rlist = ret[rnum]
    length = len(rlist)
    wut = [""]*length
    for i in range (0, length):
        num = rlist[i]
        if num == 0:
            g = 3
        if num == 1:
            smi = lizt[i]
            print ("There is a " + smi + " here. ")
    print (" ")
    return ret, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
    
def selfinv(rim):
    lizt = ["small wooden key", "gilded envelope"]
    rib = len(rim)
    for i in range (0, rib):
        hal = rim[i]
        if hal == 0:
            g = 4
        if hal == 1:
            namee = lizt[i] 
            print ("You are holding a " + namee + ". ")
    print (" ")
    return rim
    
def dropfunc(movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10):
    ent2 = movescript[1]
    lizt = ["small wooden key", "gilded envelope"]
    if ent2 == "key" or ent2 == "envelope":
        g = 3
    if ent2 == "wooden" or ent2 == "gilded":
        ent3 = movescript[2]
        if ent3 == "key" or ent3 == "envelope":
            g = 3
        else:
            print ("Drop command not understood. ")
            print (" ")
            return rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
    if g == 3:
        if ent2 == "wooden" or ent2 == "key":
            obj = 0
            check = rim[0]
        else:
            obj = 1
            check = rim[1]
    if check == 0:
        print ("You are not holding that object! ")
    else:
        ret = [rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10]
        rlizzle = ret[room]
        rlizzle[obj] = 1
        namer = lizt[obj]
        print ("You are no longer holding a " + namer + ".")
        return rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
        

room = 1
ret = []
rim = []
rim = [1, 0]
ri1 = [0, 0]
ri2 = [0, 1]
ri3 = [0, 0]
ri4 = [0, 0]
ri5 = [0, 0]
ri6 = [0, 0]
ri7 = [0, 0]
ri8 = [0, 0]
ri9 = [0, 0]
ri10 = [0, 0]
values = Init()
t = Transition()
print ("You have been here before. ")
print ("You have eight turns. ")
print ("Do not disappoint me. ")
print (" ")
print ("Controls: n - north, s - south, e - east, w - west, u - up, d - down, i - inventory, l - look, drop - drop object")
print (" ")
t = Desc(room)
while True:
    move = input (": ")
    move = move.lower()
    movescript = move.split(" ")
    movescript.append(" ")
    ent1 = movescript[0]
    if ent1 == "n" or ent1 == "s" or ent1 == "e" or ent1 == "w" or ent1 == "u" or ent1 == "d":
        dire = MoveProc(ent1)
        room, pos = Movement(room, dire)
        if pos == 0:
            j = 3
        else:
            t = Desc(room)
        ret, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = inventory(room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10)
    if ent1 == "i":
        rim = selfinv(rim)
    if ent1 == "l":
        t = Desc(room)
        ret, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = inventory(room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10)
    if ent1 == "drop":
        ent2 = movescript[1]
        if ent2 == " ":
            print ("Please be more specific. What would you like to drop? ")
            print (" ")
        else:
            rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = dropfunc(movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10)
            