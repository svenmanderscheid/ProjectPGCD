import turtle as t
import math

global br, tl, colorlist, color, FONT_SIZE

FONT_SIZE = 8
br= 0 #BottomRight
tl= 0 #TopLeft

color = 0
colorlist = ["red", "green", "yellow", "blue"]


def change_color():
    global color, colorlist
    color = (color + 1 ) % 4
    t.pencolor("Black")
    t.fillcolor(colorlist[color])

def move(count):
    global br, tl
    t.up()
    if count%2 !=0:
        t.goto(br)
    else:
        t.goto(tl)
    t.down()

def writetext(b):
    global FONT_SIZE
    t.left(45)
    x = int(math.sqrt((b**2+b**2)/4))
    y = int(b/2-FONT_SIZE) #Trouver le millieu vertical en respectant la taille de la police
    t.forward(x)
    t.write(int(b/multiplier),font=("Arial",FONT_SIZE+3,"normal"))
    t.backward(x)
    t.right(45)
    t.down()

def drawoutersquare(a, b):
    for _ in range (2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)

def drawsquare(a,b,i,count):
    t.begin_fill()
    change_color()
    for j in range(i):
        global bl, br, tl, tr
        bl = t.pos()
        t.forward(b)
        br = t.pos()
        t.left(90)
        t.forward(b)
        tr = t.pos()
        t.left(90)
        t.forward(b)
        tl = t.pos()
        t.left(90)
        t.forward(b)
        t.up()
        t.left(90)
        writetext(b)
        move(count)
    t.end_fill()

#a=int(input("Quel est votre longueur?"))
#b=int(input("Quel est votre largueur?"))

a=21
b=15

multiplier= 600//a #pour agrandir l'apparences des carrés

a=a*multiplier
b=b*multiplier


t.speed(10)
t.penup()
t.right (180)
t.forward(a//2)
t.right (180)
t.pendown()


drawoutersquare(a,b)
r = 0
count = 1 #check if we need to move right or up(even = right/odd = up)
while b > 0:
    if a > b:
        i = a // b # how many entire squares fit into the big on
        r = a % b
        drawsquare(a,b,i,count)
        count = count +1
        a = b
        b = r
print("Le PGCD est: ", a // multiplier)

t.ht()
t.done()