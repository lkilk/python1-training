birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)
#if 1946 <= birth_year <= 1965:
if birth_year >= 1946 and birth_year <= 1965:
    print("Baby Boomer")
elif birth_year >= 1966 and birth_year <= 1976:
    print("Generation X")
elif birth_year >= 1977 and birth_year <= 1994:
    print("Millennial")
elif birth_year >= 1995:
    print("Generation Z")