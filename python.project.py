#project 1:

import turtle

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()


#project 2:

import secrets
import string


def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = " "
    pw_strong = False

    while not pw_strong:
        pwd = " "
        for i in range(pw_length):
            pwd += " ".join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            pw_strong = True

   return pwd

if __name__ == '_main_':
    print(create_pw())





# project 3:


import winsound
import time


def beep_alaram():
    for repeats in range(7):
        winsound.beep(3000, 500)
        winsound.beep(6000, 300)


timeduration = int(input('duration in secound'))

hours, minutes, secounds = 0, 0, 0
for i in range(timeduration):
    print('\n' * 100)

    secounds += 1
    if secounds == 60:
        minutes += 1
        secounds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    print(str(hours) + ':' + str(minutes) + ':' + str(secounds) + ':')
    time.sleep(1)


if __name__ == '_main_':
    beep_alaram()    


