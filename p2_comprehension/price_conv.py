pounds = [10, 20, 30 , 40, 50 , 60, 70]

#create a new list of prices in dollars 
#conversion rate is 1.38 

dollars = [p*1.2 for p in pounds if p < 60] #list comprehension
print(dollars) 


names = ['David Beckham', 'George Best', 'Janet Jackson', 'James Brown']

first_names = [n.split(' ')[0] for n in names]
print(first_names)

usnames = ('Best', 'Brown')

first_names = [n.split(' ')[0] for n in names if n.split()[1] not in usnames ] 
print(first_names)

dollar = {p:p * 1.2 for p in pounds} #dictionary comprehension 
print(dollar)

names = ['David Beckham', 'George Best', 'Janet Jackson', 'James Brown']
surnames = ['Beckham', 'Best', 'Jackson', 'Brown']

for item in zip(names, surnames):
    print(item)

full_names = [names + " " + surnames for names, surnames in zip(names, surnames) if surnames not in usnames ]   
print(full_names)