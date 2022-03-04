def search_pax(pax_list, Id):
    for pax in pax_list:
        if pax["id"] == Id:
            return pax
    else:
        return None

def filter_pax(pax_list, ff, fv):
    matching_passengers = []
 
    if ff == "visited_countries":
        matching_passengers = [p for p in pax_list if fv in p[ff]]
    elif ff == "source" or ff == "dest":
        matching_passengers = [p for p in pax_list if p["flight"][ff] == fv]
    elif ff == "flight_time":
        # assuming a threshold of +/- 1 hour
        matching_passengers = [p for p in pax_list if p[ff] <= (fv + 1) and p[ff] >= (fv - 1)]
    else:
        matching_passengers = [p for p in pax_list if p[ff] == fv]

    return matching_passengers
	
def format_pax(pax_list):
    rows = []
    rows.append(f"{'ID':3}  {'Last Name':10}  {'First Name':10}  {'Source':15}  {'Dest':15}")
    for p in pax_list:
        rows.append(f"{p['id']:<3}  {p['lname']:10}  {p['fname']:10}  {p['flight']['source']:15}  {p['flight']['dest']:15}")
    return "\n".join(rows)

def read_pax_from_json(path):
    import json
    with open(path) as file:
        pax_list = json.load(file)
    return pax_list

def write_pax_to_db(pax_list):
    import sqlite3
    with sqlite3.connect("paxdb") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""create table if not exists passenger (
                                passenger_id integer, 
                                fname text, 
                                lname text)""")
            records = [(p["id"], p["fname"], p["lname"]) for p in pax_list]
            cursor.executemany("insert into passenger values (?, ?, ?)", records)
        except Exception as e:
            conn.rollback()
            print(f"Failed to write passengers to the database: {e}")
        else:
            conn.commit() 
            print("Done writing passengers to the database!") 