import unittest

from problema2 import verificarNumero


class Test(unittest.TestCase):
    def test_verificarNumero(self):
        self.assertEqual("impar",verificarNumero(int(57)))
    
if __name__ == "__main__":
    unittest.main()