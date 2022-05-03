import unittest
from services import IconService
from tkinter import Tk
from PIL import ImageTk


class TestIconService(unittest.TestCase):
    def setUp(self):
        self.window = Tk()
        self.icon_service = IconService()

    def test_icon_service_exists(self):
        self.assertNotEqual(self.icon_service, None)

    def test_get_icon(self):
        value = self.icon_service.geticon("10d")
        self.assertEqual(isinstance(value, ImageTk.PhotoImage), True)
        self.window.destroy()
