import unittest
import util

class TestUtilMethods(unittest.TestCase):

  def test_hex_to_base64(self):
      input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
      self.assertEqual(util.hex_to_base64(input_string), "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

  def test_fixed_xor(self):
      input1 = "1c0111001f010100061a024b53535009181c"
      input2 = "686974207468652062756c6c277320657965"
      self.assertEqual(util.fixed_xor(input1, input2), "746865206b696420646f6e277420706c6179")

  def test_score_englishness(self):
      strings = ['asdasdasasdasdasdasdasd', "this is valid english", "thiss sis sortamosky ltlle bit anglaise", "lklkljk(lkj(lkh"]
      sorted_strings = sorted(strings, key=util.score_englishness)
      self.assertEqual(sorted_strings, ["lklkljk(lkj(lkh", "asdasdasasdasdasdasdasd", "thiss sis sortamosky ltlle bit anglaise", "this is valid english"])

if __name__ == '__main__':
    unittest.main()