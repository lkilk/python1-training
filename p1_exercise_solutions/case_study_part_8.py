from case_study_part_8_functions import search_pax, filter_pax, format_pax, read_pax_from_json, write_pax_to_db

pax_list = read_pax_from_json("pax_list.json")
while True:
    option = input("[s]earch or [f]ilter: ")
    if option == "s":
        Id = input("Enter the passenger ID: ")
        try:
            Id = int(Id)
        except:
            print(f"Invalid passenger ID: {Id} is not a number")
        else:
            pax = search_pax(pax_list, Id)
            if pax:
                print(pax["fname"], pax["lname"])
            else:
                print("Passenger not found")
    if option == "f":
        ff = input("Enter the filter field (fname, lname, checked_bags, visited_countries, source, dest, flight_time): ")
        fv = input("Enter the filter value: ")
        if ff == "checked_bags":
            fv = bool(fv)
        try:
            if ff == "flight_time":
                fv = float(fv)
        except:
            print(f"Invalid flight time: {fv} is not a number")
            continue
        matching_passengers = filter_pax(pax_list, ff, fv)
        if matching_passengers:
            matching_passengers.sort(key=lambda p: p["lname"])
            print(format_pax(matching_passengers))
            to_db = input("Write to DB? (y/n): ")
            if to_db == "y":
                write_pax_to_db(matching_passengers)
        else:
            print("No matching passengers found")
    more = input("More? (y/n): ")
    if more == "n":
        break