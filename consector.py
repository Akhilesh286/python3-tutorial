"""class sample :
    def __init__(self):
        print ("helo")

x=sample()
y=sample()



class sample :
     def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print ('name='+self.name)
        print ("age ="+str(self.age))
        print ("place = "+self.place)

x=sample('akhil',13,'nemmara')
#y=sample()
# add age year

class sample :
    year=2020
    def __init__(self,name,age,place):
         self.name=name
         self.age=age
         self.place=place

    def add_age(self):
        self.age=self.age+1

    def place (self):
        self.place=place
        
    def display (self):
        print ("year = "+ str (sample.year))
        print ('name='+self.name)
        print ("age ="+str(self.age))
        print ("place = "+self.place)

x=sample('akhil',13,'nemmara')
y=sample('akhil',13,'nemmara')
print ("---------------")
sample.year=sample.year+1
x.add_age()
y.add_age()

x.display()
y.display()
"""

"""class sample :
    def __init__(self):
        print ("helo")

x=sample()
y=sample()


"""


# creat a function add year

class sample :
    year=2020
    def __init__(self,name,age,place):
         self.name=name
         self.age=age
         self.place=place

    def add_age(self):
        self.age=self.age+1

    def place (self):
        self.place=place
        
        
    def display (self):
        print ("year = "+ str (sample.year))
        print ('name='+self.name)
        print ("age ="+str(self.age))
        print ("place = "+self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1
            


    
x=sample('akhil',13,'nemmara')
y=sample('akhil',13,'nemmara')
print ("---------------")
sample.year=sample.year+1
x.add_age()
y.add_age()

x.display()
y.display()




print ("-----------------------------") 

sample.add_year()

x.add_age()



y.add_age()

x.display()

y.display()















