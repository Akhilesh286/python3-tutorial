"""
class sample:
    def name (self,name):
        self.name=name

first=sample()
secound=sample()
last=first+secound
"""
"this is eroar"
class sample:
    def name (self,name):
        self.name=name
    def __add__(self,other):
        name=self.name+other.name
        return name
        
first=sample()
secound=sample()
first.name("alhil")
secound.name("esh")
last=first+secound
print (last)


