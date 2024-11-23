def is_even(num):
    # "%" this operator give reminder so if the number is even and divided by two ther reminder will always be zero so in that
    # case we return true otherwise number is odd and return flase
    if(num%2==0):
        return True
    else:
        return False
    

print(is_even(9))