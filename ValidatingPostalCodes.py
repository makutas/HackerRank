"""
A valid postal code P have to fulfil both requirements below:
P must be a number in the range from 100 000 to 999 999 inclusive.
P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating
repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:
121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:
regex_integer_in_range should match only integers range from 100 000 to 999 999 inclusive.
regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
Both these regular expressions will be used by the provided code template to check if the input string  is a valid
postal code using the following expression:
"""

regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

import re

P = input('Enter postal code: ')

print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
