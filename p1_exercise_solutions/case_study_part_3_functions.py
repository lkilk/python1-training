def search_pax(pax_list, Id):
    for pax in pax_list:
        if pax["id"] == Id:
            return pax
    else:
        return None

def filter_pax(pax_list, ff, fv):
    matching_passengers = []
    for pax in pax_list:
        if ff == "visited_countries":
            if fv in pax[ff]:
                matching_passengers.append(pax)
        elif ff == "source" or ff == "dest":
            if pax["flight"][ff] == fv:
                matching_passengers.append(pax)
        elif ff == "flight_time":
            # assuming a threshold of +/- 1 hour
            if pax[ff] <= (fv + 1) and pax[ff] >= (fv - 1):
                matching_passengers.append(pax)
        else:
            if pax[ff] == fv:
                matching_passengers.append(pax)
    return matching_passengers