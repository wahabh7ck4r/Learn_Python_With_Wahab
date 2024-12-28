import random
import string

# Required components for password
CHAR = string.ascii_letters
SPCHAR = string.punctuation
NUMBER = string.digits

# Combined pool for password generation
passwd_staff = list(CHAR) + list(SPCHAR) + list(NUMBER)

def get_passwd_length():
    """Prompt user for password length between 8 and 30."""
    while True:
        getLen = input("Enter the length of password (min 8 - max 30): ")
        if getLen.isdigit():
            getLen = int(getLen)
            if 8 <= getLen <= 30:
                return getLen
            else:
                print("Please select the length between 8 - 30.")
        else:
            print("Enter an integer between 8 - 30.")

def generate_password():
    """Generate a password containing letters, digits, and special characters."""
    length = get_passwd_length()
    
    # Ensure at least one character from each category
    password = [
        random.choice(CHAR),
        random.choice(SPCHAR),
        random.choice(NUMBER),
    ]
    
    # Fill the rest of the password with random characters from all categories
    remaining_length = length - len(password)
    password += random.choices(passwd_staff, k=remaining_length)
    
    # Shuffle the password to randomize the order
    random.shuffle(password)
    
    return ''.join(password)

# Generate and print the password
password = generate_password()
print("Your Password: ", password)
