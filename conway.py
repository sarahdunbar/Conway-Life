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
                print ("Oh dear, you don't have enough attribute points for that! Please select again! ")
                print (" ")
                num = num + ent
            else:
                e = 1
        print ("Points left: " + str(num))
        list1[x] = ent
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
    
def Desc(room, ede, ba):
    if room == 1:
        print ("Courtyard Proper")
        print ("You are standing outside a spindly northern tower with a stained glass door. Around you, "
        + "an endless sea of grass ripples in the wind. It is eerily green, almost neon in its brightness. " +
        "Aside from overgrown paths east and west through the tresses, there is nothing for miles. " + 
        "Beside the door is a sign -I OPEN WITH A KEY-")
        print ("Directions: n, e, w")
    if room == 2:
        print ("Sasha's Courtyard")
        print ("You are standing in a flattened patch of grass known as Sasha's Courtyard. " +
        "Around you, the green grass extends almost to your head. A path winds east through the jade ocean towards " +
        "what looks like a tower.")
        print ("Directions: e")
    if room == 3:
        if ba == 0:
            print ("Small Ditch")
            print ("The path east leading to the small ditch you are standing in is overgrown with moss. There is a hole " +
            "in the northern cave wall. Even in here, the grass is eerily green. ")
            print ("Directions: w, n")
        if ba == 1:
            print ("Crystal Valley")
            print ("The path east leading to the valley you are standing in is clean and well swept. " +
            "As you go deeper, the walls get progressively shinier, until it's positively glowing blue. There is a gilded hole in the " +
            "northern wall. ")
            print ("Directions: w, n")
    if room == 4:
        print ("Crystal Cave")
        print ("The passage takes you into a small cave adorned with rainbow crystals. Somehow, you think you "
        + "have seen this place before... To the east, an oaken door. Beside it, a sign. -I OPEN WITH A KEY-")
        print ("Directions: s, e")
    if room == 5:
        print ("Mineshaft")
        print ("As you walk along the rusted tracks, you get the increasing feeling that you're walking in a circle. "
        + "But then, a light ahead!")
        print ("Directions: w, e")
    if room == 6:
        print ("Atrium")
        print ("You are standing in the dark castle room known as the atrium. The only light comes from the stained " +
        "glass window of the southern door. Stairways wind up and down into blackness. ")
        print ("Directions: u, d, s")
    if room == 7:
        print ("Billiard Room")
        print ("What was once the billiard room is now grey and filled with light. Stairs wind down the stone walls into blackness. ")
        print ("But as you stand here, you here distinct whispering, almost as if something has been here before. You turn " +
        "to look, but there is nothing behind you. How odd. ")
        print ("Directions: d")
    if room == 8:
        print ("Basement")
        print ("In here, it is so dark that you can't " + 
        "see your feet in front of you. Even though there are no windows, this room is distinctly drafty. ")
        print ("Directions: u, ?")
    if room == 9:
        print ("Southern Corridor")
        print ("Somehow, you have stumbled upon a hidden corridor! The floor is "
        + "distinctly earthy, and you fear that the loose dirt ceiling will collapse on your head at any minute.")
        print ("Directions: n, s")
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

def Movement(ri7, dor, values, room, dire, turncounter):
    r1 = [6, 3, 0, 2, 0, 0]
    r2 = [0, 1, 0, 0, 0, 0]
    r3 = [4, 0, 0, 1, 0, 0]
    r4 = [0, 5, 3, 0, 0, 0]
    r5 = [0, 9, 0, 4, 0, 0]
    r6 = [0, 0, 1, 0, 7, 8]
    r7 = [0, 0, 0, 0, 0, 6]
    r8 = [0, 0, 9, 0, 6, 0]
    r9 = [7, 0, 10, 0, 0, 0]
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
        if room == 1:
            if pos == 6:
                doc = dor[0]
                if doc == 0:
                    print ("The door is locked! ")
                    turncounter = turncounter - 1
                    print (" ")
                    return room, pos, turncounter
                else:
                    p = 1
            else:
                p = 1
        if room == 4:
            if pos == 5:
                doc = dor[1]
                if doc == 0:
                    print ("The door is locked! ")
                    turncounter = turncounter - 1
                    print (" ")
                    return room, pos, turncounter
                else:
                    p = 1
            else:
                p = 1
        if room == 9:
            if pos == 10:
                bleach = ri7[0]
                if bleach == 0:
                    print ("Suddenly, everything goes ")
                    print ("Quiet. ")
                    print (" ")
                    print ("A lone voice through the shadows - 'Please, please can you give us something?'")
                    print ("'Something to do in our lonely isolation?'")
                    print ("'We do love ever so much to play billiards...' ")
                    print ("'Perhaps you could give us something to play with?'")
                    print ("'Not much... Would you?'")
                    print (" ")
                    print ("The room gets colder somehow. ")
                    print ("The voice deepens - 'Otherwise, we cannot let you pass.'")
                    print ("You feel tiny hands pushing you back, back into the corridor. Whatever was beyond, is for now out of reach. ")
                    turncounter = turncounter - 1
                    print (" ")
                    return room, pos, turncounter
                else:
                    print (" ")
                    print ("'Thank you', the frail voice whispers. ")
                    print ("From above, you hear the sound of laughter mixed with the clack of billiards long forgotten, and know that you have done well. ")
                    print (" ")
                    room = pos
                    return room, pos, turncounter
        room = pos
        return room, pos, turncounter
        
def inventory(lizt, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10):
    z = 0
    d = [0, 0, 0]
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
            z = 1
            smi = lizt[i]
            d[i] = smi
    if z == 1:
        print (" ")
        for i in range(0, length):
            smi = d[i]
            if smi == 0:
                g = 3
            else:
                print ("There is a " + smi + " here. ")
        print (" ")
        return ret, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
    else:
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
    if ent2 == "stone" or ent2 == "envelope" or ent2 == "key":
        g = 3
    elif ent2 == "small" or ent2 == "gilded" or ent2 == "wooden":
        ent3 = movescript[2]
        if ent3 == "stone" or ent3 == "envelope" or ent3 == "key":
            g = 3
        else:
            print ("Object to " + word + " not understood. ")
            turncounter = turncounter - 1  
            print (" ")
            return turncounter, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
    else:
        print ("Object to " + word + " not understood. ")
        print (" ")
        turncounter = turncounter - 1
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
        if ent2 == "wooden" or ent2 == "key":
            obj = 2
            if jj == 1:
                check = rim[2]
            if jj == 2:
                check = rlizzle[2]
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
        
        
def openi (dor, bur, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10, ba):
    ede = 0
    ent2 = movescript[1]
    t = True
    if t == True:
        if ent2 == "small" or ent2 == "stone":
            g = 3
            obj = 0
        elif ent2 == "gilded" or ent2 == "envelope":
            g = 3
            obj = 1
        elif ent2 == "wooden" or ent2 == "key":
            g = 3
            obj = 2
        elif ent2 == "oak" or ent2 == "door":
            g = 3
            obj = 3
        else:
            print ("Object not understood. ")
            turncounter = turncounter - 1
            return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
        rlizzle = lizt[obj]
        if obj == 0 or obj == 1 or obj == 2:
            check = rim[obj]
            if check == 0:
                print ("You are not holding a " + rlizzle + "!")
                turncounter = turncounter - 1
                return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10    
        if obj == 0:
            if bur == 0:
                print ("You palm the small stone gingerly in your hands. It feels like a normal rock.")
                return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
            if bur == 1:
                print ("Following the instructions on the letter, you touch the top of the stone with your index finger and slide it open. A bright light! ")
                print ("Words appear in the air in front of you... - 'Such a small, shallow ditch it once was...' ")
                bur = 2
                ede = 1
                return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
            if bur == 2:
                print ("Even though you touch the stone, it does not open anymore. ")
                print ("Now, the only thing it's good for is as a billiard ball. ")
                return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
        if obj == 1:
            print ("You try your best, but the envelope refuses to open... You must rely on your special skills!")
            her = values[0]
            intl = values[1]
            spir = values[2]
            if intl > 9:
                print ("You think for a moment, then slide your finger under the flap of the envelope and rip. Who would have thought opening an envelope would be so easy?")
                t = 8
            elif her > 9:
                print ("This is a job for a hero! You throw the envelope on the ground and smash it until it opens. You feel proud.")
                t = 8
            elif spir > 9:
                print ("The moon... the rivers... the trees... Magically, the letter slides out of the envelope. ")
                t = 8
            print (" ")
            print ("As soon as you pull out the letter, it begins to disintigrate. Quickly, you scan it before it disappears in your hands. ")
            print ("Touch your index finger to the top and open the thing you've been holding from the beginning. Do not disappoint me. ")
            bur = 1
            rim[1] = 0
            return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
        if obj == 2:
            print ("The wooden key refuses to open. You know you're allowed to open doors, right?")
            turncounter = turncounter - 1
            print (" ")
            return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
        if obj == 3:
            if room == 4 or room == 1:
                key = rim[2]
                if key == 1:
                    if room == 1:
                        nom = 0
                    if room == 4:
                        nom = 1
                    dor[nom] = 1
                    print ("You have unlocked the door!")
                    return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
                else:
                    print ("The door is locked! ")
                    print (" ")
                    turncounter = turncounter - 1
                    return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10
            else:
                print ("What door?")
                print (" ")
                turncounter = turncounter - 1
                return dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10

amplaying = True
ba = 0
bur = 0
ede = 0
room = 1
turncounter = 0
ret = []
dor = [0, 0]
rim = [1, 0, 0]
ri1 = [0, 0, 0]
ri2 = [0, 1, 0]
ri3 = [0, 0, 0]
ri4 = [0, 0, 0]
ri5 = [0, 0, 0]
ri6 = [0, 0, 0]
ri7 = [0, 0, 0]
ri8 = [0, 0, 0]
ri9 = [0, 0, 0]
ri10 = [0, 0, 0]
values = Init()
t = Transition()
print ("You have been here before. ")
print ("You have 40 turns. ")
print ("Do not disappoint me. ")
print (" ")
print ("Controls: n - north, s - south, e - east, w - west, u - up, d - down, i - inventory, l - look, drop - drop object, grab - pick up object, open - open object")
print (" ")
lizt = ["small stone", "gilded envelope", "wooden key", "oak door"]
t = Desc(room, ede, ba)
while amplaying == True:
    turncounterz = 40 - turncounter
    print ("Turns Remaining: " + str(turncounterz))
    print (" ")
    move = input (": ")
    print (" ")
    print ("RESULT")
    print (" ")
    move = move.lower()
    movescript = move.split(" ")
    movescript.append(" ")
    ent1 = movescript[0]
    if ent1 == "n" or ent1 == "s" or ent1 == "e" or ent1 == "w" or ent1 == "u" or ent1 == "d":
        dire = MoveProc(ent1)
        room, pos, turncounter = Movement(ri7, dor, values, room, dire, turncounter)
        if pos == 0:
            j = 3
        else:
            t = Desc(room, ede, ba)
        ret, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = inventory(lizt, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10)
        turncounter = turncounter + 1
    elif ent1 == "i":
        rim = selfinv(lizt, rim)
    elif ent1 == "l" or ent1 == "look":
        t = Desc(room, ede, ba)
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
    elif ent1 == "open":
        ent2 = movescript[1]
        if ent2 == " ":
            print ("Please be more specific. What would you like to open?")
            turncounter = turncounter - 1
            print (" ")
        else: 
            dor, bur, ba, ede, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10 = openi(dor, bur, turncounter, values, lizt, movescript, room, rim, ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10, ba)
            turncounter = turncounter + 1
            print (" ")
    else:
        print ("Invalid command. ")
        print (" ")
    if ede == 1:
        ri3[2] = 1
        ba = 1
        ede = 0
    if turncounter == 40:
        print ("The easy part is looking. ")
        print ("It's hard enough to find. ")
        print ("Be skilled this time, my darling. ")
        k = input ("And do not disappoint me. ")
        print (" ")
        amplaying = False
    if room == 10:
        turncountere = 40 - turncounter
        print ("You've made it through your first test. Now, time for your second. ")
        print (" ")
        run = input ("Pick a class, preferably your strongest. 'h' for heroism, 'i' for intelligence, and 's' for spirit.")
        run.lower
        while True:
            if run == "h":
                stat = turncountere + values[0]
                num = 0
                break
            elif run == "i":
                stat = turncountere + values[1]
                num = 1
                break
            elif run == "s":
                stat = turncountere + values[2]
                num = 2
                break
            else:
                print (" ")
                print ("I could not understand you. Again, again, and with haste! ")
                run = input(": ")
        print (" ")
        print ("Suddenly, the ground falls away beneath your feet and you're falling... falling... ")
        t = 0
        while t == 0:
            if num == 0:
                print ("Fear fogs your vision, and you can't see. You reach deep inside yourself to find some kind of courage... ")
                if stat > 30: 
                    k = input ("You conjure up the images of your triumphs, and wrap yourself in warmth.")
                    p = Transition()
                    print ("It's time to wake up now. ")
                    t = 1
                else:
                    k = input ("But it's too much. You give in to the terror. ")    
                    break
            if num == 1:
                print ("As you fall, you feel panic beginning to overwhelm your intellect. You struggle to focus...")
                if stat > 30: 
                    k = input ("You breathe deeply, and your head begins to clear. It's so obvious now...")
                    p = Transition()
                    print ("It's time to wake up now. ")
                    t = 1
                else:
                    k = input ("But you just can't focus. Already, you feel yourself giving in. ")
                    break
            if num == 2:
                print ("But... but this isn't possible... You feel your faith begin to fade...")
                if stat > 30: 
                    k = input ("But something is causing this, isn't it? It must have a plan in the end. You close your eyes and hope for the best. ")
                    p = Transition()
                    ("It's time to wake up now. ")
                    t = 1
                else: 
                    k = input ("Yes, the spirits have given up on you for sure. You give in to the hopelessness. ")
                    break
        if t == 0:
            p = Transition()
            print ("You have disappointed me. ")
            while True:
                print (" ")
                print ("The Void:")
                print ("There is nothing here.")
                print ("Directions: ")
                print (" ")
                k = input (": ")
        if t == 1:
            print (" ")
            print ("It seems as though you are in fact worthy. Before you wake, know that you have not disappointed me. ")
            print ("Soon, you will feel the padded chair beneath your feet, the keys under your fingers...")
            print ("And now, it comes. ")
            k = input ("Hit any key to wake up. ")
            amplaying = False
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



