import unittest

from problema3 import calcularDescuento


class Test(unittest.TestCase):
    def test_calcularDescuento(self):
        self.assertEqual(("martes",5,1250.0,23750.0),calcularDescuento(float(25000),"m"))
    
if __name__ == "__main__":
    unittest.main()