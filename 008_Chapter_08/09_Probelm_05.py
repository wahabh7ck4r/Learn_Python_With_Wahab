# plaindrom is a staring that is same if we reversed it - like (lol, level etc.)


def is_Plaindrome(string):
    reversed_string = string[::-1]

    if(string == reversed_string):
        return True
    else:
        return False
    

check = is_Plaindrome("lol")
print(check)