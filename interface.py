import tkinter as tk
from tkinter import ttk

def printnumbers():
    print(f"A: {number_a.get()}")
    print(f"B: {number_b.get()}")

root = tk.Tk() #Define TK OBJECT --> Window

maina = ttk.Frame(root)
mainb = ttk.Frame(root)
maina.pack(side="left",fill="both",expand=True)
mainb.pack(side="left",fill="both",expand=True)
root.title("Visualisation PGCD") #Window Title

number_a = tk.StringVar()
number_b = tk.StringVar()

btn_calculate = ttk.Button(root, text ="Greet",command=printnumbers)
btn_calculate.pack(pady="50")

label_a = ttk.Label(maina, text="Enter a value for the first Number: ")
label_a.pack(side="top", padx=(0,0))
entry_a = ttk.Entry(mainb, width=15, textvariable=number_a)
entry_a.pack(side="top")
entry_a.focus()
label_b=ttk.Label(maina, text="Enter a value for the second Number: ")
label_b.pack(side="top", padx=(0, 0))
entry_b = ttk.Entry(mainb, width=15, textvariable=number_b)
entry_b.pack(side="top")
entry_b.focus()

root.mainloop() #Code will be running