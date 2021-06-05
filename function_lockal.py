
def chek ():
    def local():
        test=' local'
        print (test)
    def non_local():
        test='non local'
        print (test)
    def global1():
        test='global'
        print (test)


# non local


def chek ():
    def local():
        test=' local'
        print (test)
    def non_local():
        nonlocal test
        test='non local'
        print (test)
    def global1():
        test = 'glonal'
        print (test)
    test = 'defalt'
    print (test)

    non_local()
chek()



# global

def chek ():
    def local():
        test=' local'
        print (test)
    def non_local():
        test='non local'
        print (test)
    def global1():
        global test
        test = 'global'
        print (test)
    global1()
    print (test)
    

chek()

print (test)






