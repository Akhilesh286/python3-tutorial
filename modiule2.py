import modiule1

print (__name__)


modiule1.mod(10)


print (modiule1.__name__)

#or 

check = modiule1.mod

check(-10)


# or you got the function onley

from modiule1 import mod


mod (-100)



# you want to change the modiule name use the  as keyword

import modiule1 as m1

m1.mod(100)


# you want to change the function name use the as keyword

from modiule1 import mod as md

md(-13)













