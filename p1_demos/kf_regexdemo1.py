# A regular expression is a text string containing characters that will be
# translated/processed in a special way. Regular Expression support
# will be found in most programming languages. Regular expressions
# allow you to apply very powerful pattern matching options.
natinsnr_pattern = "^[A-Z]{2}[0-9]{6}[A-Z]$"

import re

# re.match will return a match object if pattern matches otherwise will return None

while True:

    # A national insurance number will always match the following format: AA999999A
    nat_ins_nr = input('Enter a national insurnamce number: ')
    mo = re.match(natinsnr_pattern , nat_ins_nr)

    if mo:
        print(f"{nat_ins_nr} is valid")
    else:
        print(f"{nat_ins_nr} is invalid")

    more = input("More? (y/n): ")
    if re.search("^(n|no|q|quit)$" , more, re.I ):
        break