from case_study_part_7_functions import search_pax, filter_pax, format_pax, read_pax_from_json

pax_list = read_pax_from_json("pax_list.json")
while True: 
    option = input("[s]earch or [f]ilter: ")
    if option == "s":
        Id = input("Enter passenger ID: ")
        try:
            Id = int(Id)
        except: 
            print(f"Invalid passednger ID: {Id} is not a number.")
        else: 
            pax = search_pax(pax_list, Id)
            if pax:
                print("Passenger Name: ", pax["fname"], pax["lname"])
            else:
                print("Passenger not found.")
    if option == "f":
        ff = input("Input the filter field (fname, lname, checked_bags, visited_countries, source, dest, flight_time): ")
        fv = input("Input filter value: ")
        if ff == "checked_bags":
            fv = bool(fv)
        if ff == "flight_time":
            try:
                fv = float(fv)
            except: 
                print(f"Invalid Flight time: {fv} is not a number.")
                continue
        matching_passengers = filter_pax(pax_list, ff, fv)
        if matching_passengers:
            matching_passengers.sort(key=lambda p: p["lname"])
            print(format_pax(matching_passengers))
        else:
            print("No passengers found")

    more = input("Continue searching/ filtering? (y/n)")
    if more.lower() == "n":
        break