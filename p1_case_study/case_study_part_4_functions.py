
def search_pax(pax_list, pax_id):
    for pax in pax_list:
        if pax["id"] == pax_id:
            return pax
        else:
            return None

def filter_pax(pax_list, ff, fv):
    
    if ff == "visited_countries":
        matching_passengers = [p for p in pax_list if fv in p[ff]]         
    elif ff == "source"  or ff == "dest":
         matching_passengers = [p for p in pax_list if p["flight"][ff] == fv]
    elif ff == "flight_time":
        #  Threshold of +/- 1 hr
        matching_passengers = [p for p in pax_list if p[ff] <= (fv + 1) and p[ff] >= (fv - 1)]
    else:
        matching_passengers = [p for p in pax_list if p[ff] == fv]
    return matching_passengers
    