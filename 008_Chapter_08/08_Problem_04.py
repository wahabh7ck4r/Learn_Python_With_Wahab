#factorial is multiply by minus one until 1 symobol to represenyt ---> ! 
#5! ==== 5 x 4 x 3 x 2 x 1  and also factorial of zero and one is 1.


def calculate_factorial(num):
    # check parameters 
    if num == 0 or num == 1:
        return 1 
    

    factorial = 2
    
    for i in range(2, num):
        print( i+1)
        factorial *= (i + 1)

    return factorial

print(calculate_factorial(5))


# optional ( extra work )

# you can also calculate factorail and it's very common way by using recursion(is a function that repeat it self.)
# your task to calculate the factorail by using recursion aslo try to drwa on paper to better understan.