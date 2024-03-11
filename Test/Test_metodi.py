import unittest
from src.Metodi import saluta, somma

class MyTestCase(unittest.TestCase):
    def test_saluta(self):
        self.assertEqual(saluta("Marco"), "Ciao, Marco!")

    def test_somma(self):
        self.assertEqual(somma(2, 3), 5)
        self.assertEqual(somma(10, -5), 5)

if __name__ == '__main__':
    unittest.main()
