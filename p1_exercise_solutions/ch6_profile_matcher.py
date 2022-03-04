def build_profile():
    profile = {
        "age": 0,
        "hobbies": []
    }

    p_age = input('Please enter age: ')
    p_age = int(p_age)
    profile["age"] = p_age

    while True:
        hobby = input('Enter a hobby: ')
        profile['hobbies'].append(hobby)

        more = input('More hobbies? (y/n):')
        if more == "n":
            break

    return profile
    
def match(p1, p2):
    match_quality = 0
    #  if abs( p1["age"] - p2["age"] ) <= 5:
    if p1["age"] >= (p2["age"] - 5) and p1["age"] <= (p2["age"] + 5):
        match_quality += 1

    for hobby in p1["hobbies"]:
        if hobby in p2["hobbies"]:
            match_quality += 1
            
    return match_quality