# # You are given two sets of student names. The first set, math_students , contains the names of
# students enrolled in a math course, and the second set, physics_students , contains the names
# of students enrolled in a physics course.
# Find and print:
# Students enrolled in both courses (intersection).
# Students enrolled in only one course (symmetric difference).
# All students enrolled in either of the courses (union).



math_students = {"hammad", "zaynab", "wahab", "afnan", "rida"}
physics_students = {"wahab", "zaynab", 'kashan', "noor"}


# get the name of those student how enrolled in both courses ( phy and math)
both_courses = math_students.intersection(physics_students)
print("Students enrolled in both courses", both_courses)


# symmetric difference : " the symmetric difference excludes the elements both sets share and keeps only those that are unique to each set"

symt_diff = math_students ^ physics_students
print("unique student: ", symt_diff)

# all students (union)

all_std = math_students.union(physics_students)
print("student enrolled either math or phy " , all_std)