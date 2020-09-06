import unittest

from problema1 import calcularEdad2070


class Test(unittest.TestCase):
    def test_calcularEdad(self):
        self.assertEqual(70,calcularEdad2070(20,2020))
    
if __name__ == "__main__":
    unittest.main()