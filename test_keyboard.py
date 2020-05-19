import unittest
import tkinterTestCase
import calculator

from tkinter import *
from tkinter import ttk

class TestKeyboard(tkinterTestCase.TkTestCase):
    def setUp(self):
        self.k = calculator.Keyboard(self.root)
        self.k.pack()
        self.k.wait_visibility()

    def tearDown(self):
        self.k.update()
        self.k.destroy()

    def test_render_Ok(self):
        self.assertEqual(self.k.winfo_height(),250)
        self.assertEqual(self.k.winfo_width(), 272)
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.children), 18)

    def test_render_roman_Ok(self):
        teclado_romano = calculator.Keyboard(self.root, "R")
        self.assertEqual(self.k.winfo_height(),250)
        self.assertEqual(self.k.winfo_width(), 272)
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.children), 13)


if __name__ == '__main__':
    unittest.main()