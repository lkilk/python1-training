from pax_list import pax_list 

while True: 
    option = input("[s]earch or [f]ilter: ")
    if option == "s":
        Id = int(input("Enter passenger ID: "))

        for passenger in pax_list:
            if passenger["id"] == Id:
                print("Passenger Name: ", passenger["fname"], passenger["lname"])
                break
            else:
                print("Passenger not found.")
    if option == "f":
        ff = input("Input the field you would like to filter: ")
        fv = input("Input filter value: ")
        if ff == "checked_bags":
            fv = bool(fv)
        if ff == "flight_time":
            fv = float(fv)
        for passenger in pax_list:
            if ff == "visited_countries":
                if fv in passenger[ff]:
                    print("Passenger Name: ", passenger["fname"], passenger["lname"])
            elif ff == "source"  or ff == "dest":
                if passenger["flight"][ff] == fv:
                    print("Passenger Name: ", passenger["fname"], passenger["lname"])
            elif ff == "flight_time":
                #  Threshold of +/- 1 hr
                if passenger[ff] <= (fv + 1) and passenger[ff] >= (fv - 1):
                    print("Passenger Name: ", passenger["fname"], passenger["lname"], '\n',
                    "Flight Time: ", passenger["flight_time"])
        for passenger in pax_list: 
            if passenger[ff] == fv: 
                print("Passenger Name: ", passenger["fname"], passenger["lname"], '\n',
                "Bags checked?: ", passenger["checked_bags"])

    more = input("Continue searching/ filtering? (y/n)")
    if more.lower() == "n":
        break
