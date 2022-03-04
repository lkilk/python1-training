class TrainingCourse:

    def __init__(self, title, duration=3, pricePerPerson=150):
        self.title = title
        self.duration = duration
        self.pricePerPerson = pricePerPerson
        self.delegates = []

    def assign_delegate(self, name):
        self.delegates.append(name)

    def getTotalRevenue(self):
        return self.pricePerPerson * len(self.delegates)

python1 = TrainingCourse('Python Programming 1', pricePerPerson=100)

print(f'\nTitle: {python1.title} - Price Per Person: {python1.pricePerPerson} - Duration(days): {python1.duration}\n')

python1.assign_delegate('Dave')
python1.assign_delegate('Sarah')
python1.assign_delegate('Tim')

print(f'\nTotal Revenue: {python1.getTotalRevenue()}')