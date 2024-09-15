# Define the form template with placeholders
form_template = """
================================
        User Registration
================================

Full Name       : [FULL_NAME]
Email Address   : [EMAIL]
Phone Number    : [PHONE]
Age             : [AGE]
Gender (M/F)    : [GENDER]

================================
       Submit your details
================================
"""

# Collect user input
full_name = input("Enter your full name: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")
age = input("Enter your age: ")
gender = input("Enter your gender (M/F): ")

# Replace placeholders using replace()
form_template = form_template.replace("[FULL_NAME]", full_name)
form_template = form_template.replace("[EMAIL]", email)
form_template = form_template.replace("[PHONE]", phone)
form_template = form_template.replace("[AGE]", age)
form_template = form_template.replace("[GENDER]", gender)

# Print the filled form
print(form_template)
