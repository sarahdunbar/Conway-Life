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

sprite1 = 0
print ("By 207, the Miori-Ethrian war had reached new heights of hostility. The mages, so eager to fight when the war" +
" had first begun in 148, have largely been wiped out. Now, both the Miorians and Ethrians have turned to " + 
"magical children as young as six years old to aid in their efforts. Drafting is not voluntary.")
print (" ")
print ("In this story, you will be playing the part of a novice soldier as they rise through the ranks of the Miorian Army. Although young, you are " +
"more than ready to fight and beat those dirty Ethrians back to where they belong. At least, you think you are.")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
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
#brave = 0
#ten = 0
#wis = 0
#clev = 0
#wit = 0
#luck = 0
#beg = 0
#amb = 0
#bea = 0
#opt = 0
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
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
mag = values[0]
con = values[2]
beg = values[9]
i = 0
r = 0
if con < 10:
    reas1 = "have few connections in high places, "
    i = 1
elif mag < 10:
    reas1 = "have shown little magical prowess, "
    i = 1
elif beg < 10:
    reas = "are about as persuasive as a rock, "
    i = 1
if i == 1:
    print ("Because you " + reas + "you are forced to bunk in the lower quarters of the academy. " +
    "As a result, you may not be immediately alerted to events. ")
    bunk = 0
elif con > 20:
    reas = "have more than a few connections with the higher-ups"
    r = 1
elif mag > 20:
    reas = "are one of the academy's top magical prospects"
    r = 1
elif beg > 20:
    reas = "are ever so persuasive"
    r = 1
if r == 1:
    print ("Because you " + reas + ", you are graciously invited into the highest tower of the academy. "
    + "Such grandeur! Such knowledge! ")
    bunk = 2
if i == 0 and r == 0:
    print ("Because you are a middling student, you bunk in an average room. Not bad for a newbie...")
    if values[8] > 20 or values[5] > 20:
        print ("...but at the same time you can't help but feel disappointed that you're not the headmaster's favorite. "
        + "After all, how else will you make it here?")
    bunk = 1
