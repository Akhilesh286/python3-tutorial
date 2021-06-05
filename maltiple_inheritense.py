"""
class first :
    def first_display (self):
        print ("first")

class secound :
    def secound_display (self):
        print ("secound_display")

class last (first,secound):
    def last (self):
        print ("last")


x=last()
x.secound_display()
x.first_display()

"""


class first :
    def first_display (self):
        print ("first")

class secound(first) :
    def secound_display (self):
        print ("secound_display")

class last (secound):
    def last (self):
        print ("last")
x=last()
x.secound_display()
x.last()

# you want to know the which is call the 
# inheritnse same find 
print (last.mro)



