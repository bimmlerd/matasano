import util
import string
import sys

def single_byte_xor(input_string : "str"):
    best_score = -sys.maxsize -1
    for key in string.printable:
        try:
            plaintext = util.utf8hex_to_ascii(util.single_byte_xor(input_string, key))
        except UnicodeDecodeError:
            continue
        except ValueError:
            continue

        score = util.score_englishness(plaintext)
        if (score) > best_score:
            best_score = score
            solution = plaintext

    return solution