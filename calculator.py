from tkinter import *
from tkinter import ttk

dbuttons = [
    {
        "text": "1",
        "col": 0,
        "row": 4,
        "cmd": lambda: Controlator.pinta("1")
    },
    {
        "text": "2",
        "col": 1,
        "row": 4,
        "cmd": lambda: Controlator.pinta("2")
    },
    {
        "text": "3",
        "col": 2,
        "row": 4,
        "cmd": lambda: Controlator.pinta("3")
    },
    {
        "text": "+",
        "col": 3,
        "row": 4,
        "cmd": lambda: Controlator.pinta("+")
    },
    {
        "text": "4",
        "col": 0,
        "row": 3,
        "cmd": lambda: Controlator.pinta("4")
    },
    {
        "text": "5",
        "col": 1,
        "row": 3,
        "cmd": lambda: Controlator.pinta("5")
    },
    {
        "text": "6",
        "col": 2,
        "row": 3,
        "cmd": lambda: Controlator.pinta("6")
    },
    {
        "text": "-",
        "col": 3,
        "row": 3,
        "cmd": lambda: Controlator.pinta("-")
    },
    {
        "text": "7",
        "col": 0,
        "row": 2,
        "cmd": lambda: Controlator.pinta("7")
    },
    {
        "text": "8",
        "col": 1,
        "row": 2,
        "cmd": lambda: Controlator.pinta("8")
    },
    {
        "text": "9",
        "col": 2,
        "row": 2,
        "cmd": lambda: Controlator.pinta("9")
    },
    {
        "text": "x",
        "col": 3,
        "row": 2,
        "cmd": lambda: Controlator.pinta("x")
    },
    {
        "text": "C",
        "col": 1,
        "row": 1,
        "cmd": lambda: Controlator.pinta("C")
    },
    {
        "text": "+/-",
        "col": 2,
        "row": 1,
        "cmd": lambda: Controlator.pinta("+/-")
    },
    {
        "text": "÷",
        "col": 3,
        "row": 1,
        "cmd": lambda: Controlator.pinta("÷")
    },
    {
        "text": "0",
        "col": 0,
        "row": 5, 
        "W": 2,
        "cmd": lambda: Controlator.pinta("0")
    },
    {
        "text": ",",
        "col": 2,
        "row": 5,
        "cmd": lambda: Controlator.pinta(",")
    },
    {
        "text": "=",
        "col": 3,
        "row": 5,
        "cmd": lambda: Controlator.pinta("=")
    }
]

def pinta(valor):
    print(valor)
    return valor

class Controlator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=300)
        d = Display(self)
        d.grid(column=0, row=0, columnspan=4)

        for properties in dbuttons:
            btn = CalcButton(self, properties['text'], pinta, properties.get("W", 1), properties.get("H", 1))
            btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))

    @classmethod
    def pinta(cls, valor):
        print(valor)
        return valor

class Display(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=50)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')

        lbl = ttk.Label(self, text="0", anchor=E, style='my.TLabel')
        lbl.pack(side=TOP, fill=BOTH, expand=True)

    

class Selector(ttk.Radiobutton):
    pass

class CalcButton(ttk.Frame):
    def __init__(self, parent, value, command, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=68*width, height=50*height)
        self.pack_propagate(0)

        btn = ttk.Button(self, text=value, command=lambda: command(value))
        btn.pack(side=TOP, fill=BOTH, expand=True)

