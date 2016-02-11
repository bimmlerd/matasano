import unittest
from single_byte_xor import single_byte_xor

class TestUtilMethods(unittest.TestCase):

  def test_single_byte_xor(self):
      input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
      self.assertEqual(single_byte_xor(input_string), "solution")

if __name__ == '__main__':
    unittest.main()