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
def Gender (gender, sprite1):
    if gender == "male":
        print ("A male, I see. Good, good. ")
        sprite1 == 1
    if gender == "female":
        print ("A female, I see. Good, good. ")
        sprite1 == 2
    else: 
        print ("Sorry, I didn't catch that. Oh well, gender doesn't matter that much anyways. ")
        sprite1 == 3

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
gender = input ("And... are you a boy or a girl? Type *male* for male and *female* for female. ")
gender = Gender(gender, sprite1)
print (" ")
print (name + " will have 50 attribute points to spend on ten categories: ")
