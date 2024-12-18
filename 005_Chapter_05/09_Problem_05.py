# taking student grade as an inpute 
wahab = input("Enter you grade: ")
kashan = input("Enter you grade: ")
sajid = input("Enter you grade: ")
hammad = input("Enter you grade: ")
tony = input("Enter you grade: ")

# create an empty dictioay so we can store studnet grade in them 
student_grades = {}

# adding value to dictiaony
student_grades["wahab"] = wahab
student_grades["kashan"] = kashan
student_grades["sajid"] = sajid
student_grades["hammad"] = hammad
student_grades["tony"] =  tony

# print the dictionary
print(student_grades)


# probelm 06 if two student have same name then what happen 
student_grades['wahab'] = input("enter your grade")
# print it again 
print(student_grades)   # it update the key that already exist in this case the grade of wahab is update they don't add anohter key as a name wahab beacuse in dictioanry key() are unique.

# probelm 07 if two student have same grade than what happed
# -- nothing happend beacuse in dictionary key are unique but value are non-singular(means are not unique).
