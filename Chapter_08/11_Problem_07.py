def concatenate_strings(*args):
    result = ""

    for string in args:
        result = result + string

    return result

print(concatenate_strings('helloooooo' ,"!", " ", "there", "."))


# there is an alternative and easy way to solve this qeustion by using built in python funtion "join".
# here the easy solution for this probelm 

def concatenate_strings(*args):
    result = "".join(args)
    return result

print(concatenate_strings('helloooooo' ,"!", " ", "there", "."))
