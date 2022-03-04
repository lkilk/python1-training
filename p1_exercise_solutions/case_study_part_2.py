from pax_list import pax_list

while True:
    option = input("[s]earch or [f]ilter: ")
    if option == "s":
        Id = input("Enter the passenger ID: ")
        Id = int(Id)
        for pax in pax_list:
            if pax["id"] == Id:
                print(pax["fname"], pax["lname"])
                break
        else:
            print("Passenger not found")
    if option == "f":
        ff = input("Enter the filter field (fname, lname, checked_bags, visited_countries, source, dest, flight_time): ")
        fv = input("Enter the filter value: ")
        if ff == "checked_bags":
            fv = bool(fv)
            print(fv)
        if ff == "flight_time":
            fv = float(fv)
        for pax in pax_list:
            if ff == "visited_countries":
                if fv in pax[ff]:
                    print(pax["fname"], pax["lname"])
            elif ff == "source" or ff == "dest":
                if pax["flight"][ff] == fv:
                    print(pax["fname"], pax["lname"])
            elif ff == "flight_time":
                # assuming a threshold of +/- 1 hour
                if pax[ff] <= (fv + 1) and pax[ff] >= (fv - 1):
                    print(pax["fname"], pax["lname"])
            else:
                if pax[ff] == fv:
                    print(pax["fname"], pax["lname"])
    more = input("More? (y/n): ")
    if more == "n":
        break