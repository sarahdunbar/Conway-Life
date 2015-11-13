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
print ("In this story, you will be playing the part of a novice teleporter as they rise through the ranks of the Miorian Army. Although young, you are " +
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
list3 = ["Bravery", "Tenacity", "Wisdom", "Cleverness", "Wit", "Luck", "Beguiling", "Ambition", "Beauty", "Optimism"]
for i in list3:
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
list2 = ["Bravery is the ability to act in a situation. ", "Tenacity is the ability to withstand pain. ", "Wisdom is the ability to acquire and recall knowledge, as well as the knowledge of when to use it. ", "Cleverness is the ability to solve problems quickly. ", "Wit is the ability to make friends and be liked. ", "Luck is a natural gift not quite described. ", "Beguiling is the ability to change minds. ", "Ambition is the drive to excel and go beyond. ", "Beauty is a natural appearance and charm. ", "Optimism is the ability to see the best in a bad situation. "]
#list2 = [brave, ten, wis, clev, wit, luck, beg, amb, bea, opt]
for x in range (0, 10):
    desc = list2[x]
    print (desc)
    namre = list3[x]
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
        


