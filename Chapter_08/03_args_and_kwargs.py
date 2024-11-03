# imagine when you need multiple input in muction but you don't know the exac amoutn so what will you do ? 
# don't we're we've have solution for all things,In python there is a concept of args an kwargs so let's disscuss in detail.
# args 

# when you only need input and know  purpose like you need multiple sutends marks. 

def marks(*args):  #this take muliple marks in tuple 
    for num in marks:
        print(num)  # print marks of every student 

marks(33,12,33,22,26)  # call the function 

# kwargs: Imagine when you need input(multiple) but you don't know their purpose that what ? 
# Don't we've have anthore solution for that also.

# kwargs take mupltiple value in dictionary(key value) pairs. 

def bioData(**kwargs):
    # print(kwargs)
    for i , j in kwargs.items(): 
        print(i, " :" , j)  # i is key, and j is value.


        print(i, " :" , j)  # i is key, and j is value.
bioData(name="wahab", No="xxxx-xxxxxxx", gender="male", age='17', status='single')




