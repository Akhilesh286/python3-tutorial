"""
class base_slass:
    def desplay(self):
        print ("welcome")


class sabe_class(base_slass):
    def hello (self):
        print ("hello")

x=base_slass()
x.desplay()
y=sabe_class()
y.desplay()
y.hello()
"""
"""
class base_slass:
    def desplay(self,name):
        self.name=name

class sabe_class(base_slass):
    def hello (self):
        print ("hello")
        print ("name= "+self.name)


y=sabe_class()
y.desplay("akhil")
y.hello()



# comsector overread

 
class base_slass:
    def __init__ (self):
        print ("base init")
    def desplay(self):
        print ("welcome")


class sabe_class(base_slass):
    def __init__(self):
        print ("sabe inite")

        
    def hello (self):
        print ("hello")




y=sabe_class()
y.desplay()
y.hello()

"""

# function inherite


class base_slass:
    def desplay(self):
         print ("base ")

class sabe_class(base_slass):

    def desplay(self):
        print ("sube")

   # def hello (self):
    #    print ("hello")
     #   print ("name= "+self.name)


y=sabe_class()
y.desplay()
#y.hello()

"you want to call the base class /function use this"
"the cament "
"super ()"
"super().__init__"
"super().desplay()""





 
