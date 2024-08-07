# Carlos Paredes Márquez
# August 7th, 2024
# Task: A valid postal code 'P' have to fullfil both below requirements:
# P must be a number in the range from 100000 to 999999 inclusive
# P must not contain more than one alternating repetitive digit pair

regex_integer_in_range = r"^([1-9]\d{5})$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

# r"^([1-9]\d{5})$", where:
# ^ since the first element 
# [1-9] must be a number from 1-9 
# \d{5} the next 5 elements could be every number from 0-9 
# $ makes sure to check the coincidente till the end

# r"(\d)\d\1", where
# (\d) capture the first digit
# (?=\d\1) lookahead, 

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)