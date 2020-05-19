from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Calculadora')
        self.geometry("272x300")
        self.pack_propagate(False)

        c = calculator.Controlator(self)
        c.pack(side=TOP, fill=BOTH)


    def main(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.main()

