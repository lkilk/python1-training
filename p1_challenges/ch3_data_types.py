id, first_name, last_name = 1234, 'John', 'Doe'
checked_bags = False
visited_countries = ['Latvia','Guyana','Yemen','Uzbekistan']
flight_details = {'outbnd':'LGW', 'dest':'CDG', 'duration':1.25}

#print(f' ID: {id} \n Full Name: {first_name} {last_name} \n Completed Bag Check? {checked_bags} \n Itinary: {visited_countries}')
#print(' Outbound Airport:', flight_details['outbnd'], '\n Destination Airport:', flight_details['dest'], 
#      '\n Flight Time:', flight_details['duration'])

print(id, type(id))
print(first_name, type(first_name))
print(last_name, type(last_name))
print(checked_bags, type(checked_bags))
print(visited_countries, type(visited_countries))
print(flight_details, type(flight_details))