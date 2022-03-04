
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

def format_pax(pax_list):
    rows = []
    rows.append(f"{'ID' :3}  {'Last Name' :10}  {'First Name' :10}  {'Source' :15}  {'Dest' :15}")
    for p in pax_list:
        rows.append(f"{p['id'] :<3}  {p['lname'] :10}  {p['fname'] :10}  {p['flight']['source'] :15}  {p['flight']['dest'] :15} ")
    return "\n".join(rows)

