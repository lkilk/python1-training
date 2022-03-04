from pax_list import pax_list

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
    filter_fields = ", ".join( pax_list[0].keys() )
    
    ff = input(f"Enter the filter field ({filter_fields}): ")
    fv = input("Enter the filter value: ")
    if ff == "checked_bags":
        fv = bool(fv)
    if ff == "flight_time":
        fv = float(fv)
    for pax in pax_list:
        if ff == "visited_countries":
            # assuming the user inputs one country only
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
                print('fv:' , fv, 'type(fv):' , type(fv) )
                print(pax["fname"], pax["lname"], pax["checked_bags"])