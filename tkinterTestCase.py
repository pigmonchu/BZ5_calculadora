import unittest
from tkinter import * 

class TkTestCase(unittest.TestCase):
    @classmethod
    def SetUpClass(cls):
        cls.root = Tk()
        cls.wait_visibility()

    @classmethod
    def TearDownClass(cls):
        cls.root.update()
        cls.root.destroy()

