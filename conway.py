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
    print ("You will have 30 attribute points to spend on six categories: ")
    namestat = ["Bravery", "Tenacity", "Wisdom", "Cleverness", "Luck", "Manipulation"]
    for i in namestat:
        print (i)
    print (" ")
    num = 30
    list1 = [0, 0, 0, 0, 0, 0]
    list2 = ["Bravery is the ability to act in a situation. ", "Tenacity is the ability to withstand pain. ", "Wisdom is the ability to acquire and recall knowledge, as well as the knowledge of when to use it. ", "Cleverness is the ability to solve problems quickly. ", "Luck is a natural gift not quite described. ", "Manipulation is the ability to change minds in ways less honorable. "]
    for x in range (0, 6):
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
    hero = [0, 1]
    intel = [3, 5]
    spir = [2, 4]
    att = ["Heroicness", "Intelligence", "Spirit"]
    nums2 = [hero, intel, spir]
    names = [0, 0, 0]
    values = [0, 0, 0]
    print (" ")
    for x in range (0, 3):
        attr = att[x]
        varlist = nums2[x]
        major = varlist[0]
        minor = varlist[1]
        majname = namestat[major]
        minname = namestat[minor]
        lvl = list1[major] + list1[minor]
        print (attr + ": " + majname + " plus " + minname + ".")
        print (attr + ": " + str(lvl))
        values[x] = lvl
        namer = input("Type anything to continue. ")
        names[x] = namer
        print (" ")
    valuez = values[:]
    val2 = valuez.sort()
    return values

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

def Movement(values, room, dire, turncounter):
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
        turncounter = turncounter - 1
        return room, pos, turncounter
    else:
        if room == 4:
            hero = values[0]
            if hero < 11:
                print (" ")
                print ("You feel your legs shaking beneath you, and realize that being heroic simply isn't your strong suit. " +
                "After all, what's the point of being the hero when you're dead?? ")
                pos = 0
                turncounter = turncounter - 1
                return room, pos, turncounter
            else:
                print (" ")
                print ("You puff up your chest and venture into the blackness. ")
        room = pos
        return room, pos, turncounter
        
def inventory(lizt, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10):
    ret = [rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10]
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
    
def selfinv(lizt, rim):
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
    
def dropfunc(turncounter, word, jj, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10):
    ret = [rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10]
    rlizzle = ret[room]
    ent2 = movescript[1]
    if ent2 == "stone" or ent2 == "envelope":
        g = 3
    if ent2 == "small" or ent2 == "gilded":
        ent3 = movescript[2]
        if ent3 == "stone" or ent3 == "envelope":
            g = 3
        else:
            print ("Object to " + word + " not understood. ")
            turncounter = turncounter - 1  
            print (" ")
            return turncounter, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
    if g == 3:
        if ent2 == "small" or ent2 == "stone":
            obj = 0
            if jj == 1:
                check = rim[0]
            if jj == 2:
                check = rlizzle[0]
        if ent2 == "gilded" or ent2 == "envelope":
            obj = 1
            if jj == 1:
                check = rim[1]
            if jj == 2:
                check = rlizzle[1]
    if check == 0:
        if jj == 1:
            print ("You are not holding that object! ")
        if jj == 2:
            print ("That object is not in this room! ")
        print (" ")
        turncounter = turncounter - 1  
        return turncounter, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
    if check == 1:
        namer = lizt[obj]
        if jj == 1:
            rlizzle[obj] = 1
            rim[obj] = 0
            print ("You are no longer holding a " + namer + ".")
        if jj == 2:
            rim[obj] = 1
            rlizzle[obj] = 0
            print ("You have picked up the " + namer + ".")
        print (" ")
        return turncounter, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
        
def use(turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10, ba):
    ent2 = movescript[1]:
        if ent2 == "small" or ent2 == "stone":
            g = 3
            obj = 0
        elif ent2 == "gilded" or ent2 == "envelope":
            g = 3
            obj = 1
        else:
            print ("Object not understood. ")
            turncounter = turncounter - 1
            return turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
        rlizzle = lizt[obj]
        check = rim[obj]
        if rim == 0:
            print ("You are not holding the " + rlizzle + ".")
            turncounter = turncounter - 1
            return turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10    
        else:
            if obj == 0:
                if ba == 0:
                    print ("You palm the small stone gingerly in your hands. It feels like a normal rock.")
                if ba == 1:
                    print ("Following the instructions on the letter, you touch the top of the stone with your index finger. A bright light! ")
            if obj == 1:
                print ("The letter refuses to open... You must rely on your special skills!")
                her = values[0]
                int = values[1]
                spir = values[2]
                if int > 12:
                    print ("You think for a moment, then slide your finger under the flap of the envelope, creasing the paper inside. Soon, you can easily pull out the letter!")
                    t = 8
                if her > 12:
                    print ("This is a job for a hero! You throw the envelope on the ground and smash it until it opens. You feel proud.")
                if 
ba = 0
room = 1
turncounter = 0
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
print ("Controls: n - north, s - south, e - east, w - west, u - up, d - down, i - inventory, l - look, drop - drop object, grab - pick up object, use - use object")
print (" ")
lizt = ["small stone", "gilded envelope"]
t = Desc(room)
while True:
    turncounterz = 8 - turncounter
    print ("Turns Remaining: " + str(turncounterz))
    print (" ")
    move = input (": ")
    move = move.lower()
    movescript = move.split(" ")
    movescript.append(" ")
    ent1 = movescript[0]
    if ent1 == "n" or ent1 == "s" or ent1 == "e" or ent1 == "w" or ent1 == "u" or ent1 == "d":
        dire = MoveProc(ent1)
        room, pos, turncounter = Movement(values, room, dire, turncounter)
        if pos == 0:
            j = 3
        else:
            t = Desc(room)
        ret, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = inventory(lizt, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10)
        turncounter = turncounter + 1
    elif ent1 == "i":
        rim = selfinv(lizt, rim)
    elif ent1 == "l" or ent1 == "look":
        t = Desc(room)
        ret, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = inventory(lizt, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10)
    elif ent1 == "drop" or ent1 == "grab":
        if ent1 == "drop":
            word = "drop"
            jj = 1
        if ent1 == "grab":
            word = "grab"
            jj = 2
        ent2 = movescript[1]
        if ent2 == " ":
            print ("Please be more specific. What would you like to " + word + "?")
            turncounter = turncounter - 1  
            print (" ")
        else:
            turncounter, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = dropfunc(turncounter, word, jj, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10)
        turncounter = turncounter + 1    
    elif ent1 == "use":
        ent2 = movescript[1]
        if ent2 == " ":
            print ("Please be more specific. What would you like to use?")
            turncounter = turncounter - 1
            print (" ")
        else: 
        turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = use(turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10, ba)
        
    else:
        print ("Invalid command. ")
        print (" ")
    if turncounter == 8:
        print ("The easy part is looking. ")
        print ("It's hard enough to find. ")
        print ("Be brave this time, my darling. ")
        print ("And do not disappoint me. ")
        print (" ")
        break
print ("Game over!")
