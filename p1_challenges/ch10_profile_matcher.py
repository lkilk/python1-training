def build_profile():
    profile = {
        "age": 0,
        "hobbies": []
        }
    p_age = int(input("Enter your age: "))
    profile["age"] = p_age

    while True:
        hobby = input("Enter a hobby: ")
        profile["hobbies"].append(hobby)
        more = input("Add another hobby? (y/n): ")
        if more.lower() == "n":
            print("Finished adding hobbies")
            break
    
    return profile

def match(p1, p2):
    match_quality = 0
    #if abs( p1["age"] - p2["age"]) <= 5:
    if p1["age"] >= (p2["age"] - 5) and p1["age"] <= (p2["age"] + 5):
        match_quality += 1
    s1 = set(p1["hobbies"])
    s2 = set(p2["hobbies"])
    s3 = s1.union(s2)
    hobbymatch = len(s3)
    match_quality += hobbymatch
    return match_quality 


