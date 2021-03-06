import sys as sys
import time as t
import string
import random as rand
import winsound as wins

invaildChars = set(string.punctuation)

HEADER = "/-----------------------------Scooby Escape 2-------------------------------\\"
TITLE = " to Scooby Escape 2! \n"
OBJ_1 = "Scooby Doo Has kidnapped you for unknown reasons.\n"
OBJ_2 = "You need to escape before he experiments on you.\n"
LINE_NORM = "-------------------------------------------------"
BEGIN = "You wake up in a room, it has a control panel with input\n"
cardsOut = []
no_option = "Loser say what? But really, say something that is understood by the program, come on man."

def typewriter(string_to_send):
    '''Write Text like a typewriter'''
    for char in string_to_send:
        t.sleep(0.1)
        sys.stderr.write(char)
        sys.stderr.flush()


def getinput(question_to_ask):
    '''Get Users Input'''
    userinput = raw_input(question_to_ask)
    return userinput.rstrip()


def countdown(time_to_wait):
    '''countdown for game'''
    for x in range(0, time_to_wait):
        print(time_to_wait)
        t.sleep(1)
        time_to_wait -= 1
    return


while True:
    USERNAME = getinput("What is your name?:")
    if any(char.isdigit() for char in USERNAME):
        print "You cant have numbers in your name silly!"
    elif any(char in invaildChars for char in USERNAME):
        print"Names don't have special characters! Try again."
    else:
        print "\n" * 100
        print HEADER
        break
typewriter(" Welcome " + USERNAME + TITLE)
print LINE_NORM
t.sleep(0.5)
typewriter(OBJ_1)
typewriter(OBJ_2)
print LINE_NORM
t.sleep(0.5)
typewriter(BEGIN)
while True:
    if getinput("Are You Ready?: ").lower() == "yes" or "ya" or "yea":
        print "Ok, First question coming right up!\n"
        break
    else:
        typewriter("Well, let's endure this together!\n")
        countdown(10)

typewriter("There are two answers that are listed, 21 and 19")
typewriter(" with a question that asks, What is 9 + 10?")
while True:
    userinputted = getinput("\n What is your answer?\n > ")
    if userinputted == "19":
        print"Correct! Continue to next room."
        break
    elif userinputted == "21":
        print"Wrong! Get out of here!"
        sys.exit(21)
    else:
        print "Error: You have inputted something incorrect!"
    typewriter("A Hidden door opens up, You walk through it.")
    #Start War game here
    typewriter("You walk into a room that has a cage with a dog in it.  Do you let it out, or do you leave it?\n")
    Q2 = getinput(">")
    if Q2.lower() == "yes" or "ya" or "yeah" or "yeah":
        print"Well that is pretty nice of you considering that you don't know the dog is really Scrappy."
    elif Q2.lower() == "no" or "naw" or "yeet" or "nope":
        print"Well that isn't very nice, you should be ashamed, unless you do not like Scrappy Doo, because that was the dog, Scrappy, the dude who is kind of cool."
        sys.exit(21)
    else:
        print(no_option)
    typewriter("You walk in a room that is full of pink.  There is a control panel that has two shapes, a maple leaf, and a star.  Which one do you pick?\n")
    Q3 = getinput(">")
    if Q3.lower() == "maple leaf":
        typewriter("Correct! Canada, and one of the devs, are proud of you! Go and get yourself a bottle of maple syrup, you earned it!")
    elif Q3.lower() == "star":
        print"Pssh, Americans...JK NO RE! But seriously, you ain't gon' continue wit dat attitude."
        sys.exit()
    else:
        print(no_option)
        sys.exit()
    Q4 = getinput("")
