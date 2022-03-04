table = ["Bath", "Derby", "Gloucester", "Lancaster", "Newcastle", "Plymouth", "Salford", "Wakefield"]

table.remove("Newcastle")
print(table)

table.insert(2, "Newcastle")
print(table)

table.remove("Derby")
table.insert(3, "Derby")
print(table)

table.remove("Salford")
print(table)

table.append("Canterbury")
print(table)

table[5] = "York"
print(table)

to_play_in_europe = table[:2]

if "Newcastle" in to_play_in_europe:
    print("Newcastle to play in Europe")

for teams in table:
    print(teams)

