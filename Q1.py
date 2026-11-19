
# Username Validation System

username = input("Enter your username: ")

# Remove unwanted spaces
clean_username = username.strip()

# Check username conditions
if clean_username == "":
    print("Invalid Username")
    print("Reason: Username cannot contain only spaces.")

elif len(clean_username) < 5:
    print("Invalid Username")
    print("Reason: Username must contain at least 5 characters.")

elif clean_username.lower() == "admin":
    print("Invalid Username")
    print("Reason: Username cannot be admin.")

else:
    print("Valid Username")
