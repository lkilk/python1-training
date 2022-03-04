class TrainingCourse:

    def __init__(self,title,duration,pricePerPerson):
        self.title = title
        self.duration = duration
        self.pricePerPerson = pricePerPerson
        self.delegates = []

    def addDelegates(self,name):
        self.delegates.append(name)
        print(self.delegates)

    def getTotalRevenue(self):
        totalRev =  len(self.delegates) * self.pricePerPerson
        print("Total Revenue = ", totalRev) 
        
course1 = TrainingCourse("Python Programming 1", 4, 1600)
course1.addDelegates("Harry")
course1.addDelegates("Steve")
course1.addDelegates("Julie")
course1.getTotalRevenue()
