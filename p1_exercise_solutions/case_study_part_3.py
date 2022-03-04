from pax_list import pax_list
from case_study_part_3_functions import search_pax, filter_pax

while True:
    option = input("[s]earch or [f]ilter: ")
    if option == "s":
        Id = input("Enter the passenger ID: ")
        Id = int(Id)
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
        if ff == "flight_time":
            fv = float(fv)
        matching_passengers = filter_pax(pax_list, ff, fv)
        if matching_passengers:
            for pax in matching_passengers:
                print(pax["fname"], pax["lname"])
        else:
            print("No matching passengers found")
    more = input("More? (y/n): ")
    if more == "n":
        break