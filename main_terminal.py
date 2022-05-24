import turtle as t
import math

global br, tl, color_list, color, FONT_SIZE

FONT_SIZE = 8
br= 0 #BottomRight
tl= 0 #TopLeft

color = 0
color_list = ["red", "green", "yellow", "orange"]


def change_color():
    global color, color_list
    color = (color + 1 ) % 4
    t.pencolor("Black")
    t.fillcolor(color_list[color])

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
    y = int(b/2-FONT_SIZE) #Trouver le millieu vertical en respectant la taille de la police
    x = int(b/2-len(str(b))/2) #Trouver le milleux horizontal en respectant la taille du chiffre
    t.up()
    t.left(90)
    t.forward(y) #Revenir au centre vertical
    t.right(90)
    t.forward(x) # Aller au centre horizontal
    if int(b/multiplier >= 10):
        t.write(int(b/multiplier),align="left",font=("Arial",FONT_SIZE))
    else:
        t.write(int(b/multiplier),align="left",font=("Arial",FONT_SIZE))
    t.backward(x) #Revenir a la bordure exterieure à gauche
    t.right(90)
    t.forward(y) #Aller en bas a gauche où on était avant
    t.left(90)
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
b=11

multiplier= 600//a #pour agrandir l'apparences des carrés

a=a*multiplier
b=b*multiplier


t.speed(1000)
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
        i = a // b # how many entire squares fit into the big one
        r = a % b
        drawsquare(a,b,i,count)
        count = count + 1
        a = b
        b = r
print("Le PGCD est: ", a // multiplier)

t.ht()
t.done()