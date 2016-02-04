import base64
import collections


def hex_to_base64(input_string: 'str') -> 'str':
    return base64.b64encode(bytes.fromhex(input_string)).decode("utf-8")


def fixed_xor(input1: 'str', input2: 'str') -> 'str':
    return hex(int(input1, 16) ^ int(input2, 16))[2:]


def score_englishness(input_string: "str") -> 'int':
    letters = collections.Counter(input_string)
    # TODO
    pass


englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}