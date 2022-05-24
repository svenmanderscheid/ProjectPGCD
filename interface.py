import tkinter as tk
from random import randint
from tkinter import *
from tkinter import ttk
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
import math

FONT_SIZE = 8
br = 0  # BottomRight
tl = 0  # TopLeft

color = 0
color_list = ["red", "green", "yellow", "orange"]


# Restriction that user only can enter Integer
class Lotfi(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit():
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)


def clear():
    number_a.delete(0, END)
    number_a.insert(0, "")


def change_color():
    global color, color_list
    color = (color + 1) % 4
    t.pencolor("Black")
    t.fillcolor(color_list[color])


def move(count):
    global br, tl
    t.up()
    if count % 2 != 0:
        t.goto(br)
    else:
        t.goto(tl)
    t.down()


def writetext(b):
    global FONT_SIZE, multiplier_b
    y = int(b / 2 - FONT_SIZE)  # Trouver le millieu vertical en respectant la taille de la police
    x = int(b / 2 - len(str(b)) / 2)  # Trouver le milleux horizontal en respectant la taille du chiffre
    t.up()
    t.left(90)
    t.forward(y)  # Revenir au centre vertical
    t.right(90)
    t.forward(x)  # Aller au centre horizontal
    if int(b / multiplier_b >= 10):
        t.write(int(b / multiplier_a), align="left", font=("Arial", FONT_SIZE))
    else:
        t.write(int(b / multiplier_a), align="left", font=("Arial", FONT_SIZE))
    t.backward(x)  # Revenir a la bordure exterieure à gauche
    t.right(90)
    t.forward(y)  # Aller en bas a gauche où on était avant
    t.left(90)
    t.down()


def drawoutersquare(a, b):
    for _ in range(2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)


def drawsquare(a, b, i, count):
    t.begin_fill()
    change_color()
    for j in range(i):
        global br, tl
        t.forward(b)
        br = t.pos()
        t.left(90)
        t.forward(b)
        t.left(90)
        t.forward(b)
        tl = t.pos()
        t.left(90)
        t.forward(b)
        t.up()
        t.left(90)
        writetext(b)
        move(count)
        print(f"Value of A = {a} and Value of B = {b}")
    t.end_fill()


def draw():
    global multiplier_a, multiplier_b
    t.reset()
    a = int(number_a.get())
    b = int(number_b.get())

    multiplier_a = int(600 / a)
    multiplier_b = int(600 / b)

    t.speed(100)
    t.penup()
    t.right(180)
    t.forward(a*multiplier_a // 2 - 50)
    t.left(90)
    t.forward(b*multiplier_a // 2)
    t.left(90)
    t.pendown()

    drawoutersquare(a * multiplier_a, b * multiplier_a)
    r = 0
    count = 1  # check if we need to move right or up(even = right/odd = up)

    while b > 0:
        if a > b:
            i = a // b  # how many entire squares fit into the big one
            r = a % b
            drawsquare(a * multiplier_a, b * multiplier_a, i, count)
            count = count + 1
            a = b
            b = r
    print("Le PGCD est: ", a)


# USER_INTERFACE
root = Tk()
can_height = 700
can_width = 1000
root.geometry(f"{can_width}x{can_height}")

# INFORMATION PANEL (Button and Inputfield)
information_panel = Frame(root)

label_a = ttk.Label(information_panel, text="Nombre entier A: ")
label_a.pack(side=TOP, padx=20, pady=0)
number_a = Lotfi(information_panel)
number_a.pack(side=TOP, padx=20, pady=10)
number_a.focus()
label_b = ttk.Label(information_panel, text="Nombre entier B: ")
label_b.pack(side=TOP, padx=20, pady=0)
number_b = Lotfi(information_panel)
number_b.pack(side=TOP, pady=10)

btn_run = Button(information_panel, text="PGCD", command=draw)
btn_run.pack(side=TOP, pady=10)

btn_clear = Button(information_panel, text="Clear", command=clear)
btn_clear.pack(side=TOP, pady=10)

information_panel.pack(side=LEFT)

canvas = Canvas(root, width=can_width, height=can_height)
canvas.pack(side=LEFT)
screen = TurtleScreen(canvas)
screen.screensize(can_width, can_height)
t = RawTurtle(canvas)

screen.mainloop()
