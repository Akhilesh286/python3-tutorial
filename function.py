
def hai():
    print ('hai')


hai()

#function with argument with return value


def hay(name):
    print (name)


hay('hai iam akhile')

# or 

a= 'king'
hay(a)


# or



b = input ('ender')

hay(b)


def hello(num,num2):
    print (num,num2)



hello(10,20)


def mor(*hai):
    print ('1th:'+hai[0]+'2th:'+hai[1])


mor('akhil','esh')

# global and local veriabile

#global


globel=10000
def sample():
    print (globel)


sample()
print (globel)

# local 


def sample1 (local):

    print (local)


sample1(5000000)

#print (local)

# print is not founted 

""" this is local this is call only  inside the
function"""



# key word argument 

def key (name,age):
    print (name,age)

key ('akhil',13)
# or 
# key argument
key (age=10,name= 'akhil')


# defalt 

def defalt (name,age=12):
    print (name,age)

defalt (name='hai')
#OR

defalt (name='hai',age=13)


# function with return value
# sum program

def sum (num1,num2):
    sum=num1+num2
    return sum

equl=sum (10,20)
print (equl)

# with out argument

number1=200
number2=100

def add ():
    add1=number2+number1
    print (add1)

    return add1




add()





















