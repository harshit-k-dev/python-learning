print("="*76)
print("Welcome to the Login Simulator!".center(76))
print("="*76)

# predefined username and password
USERNAME = "harshit"
PASSWORD = "python123"

# user_input for username and password
user_username = input("\nEnter your username: ").strip().lower()

# check if the entered username and password match the predefined ones
if user_username == USERNAME:
    user_password = input("Enter your password: ").strip()

    if user_password == PASSWORD:
        print("\nLogin successful! Welcome Harshit.")
    else:
        print("\nIncorrect password. Please try again.")
else:
    print("\nUsername not found. Please check your username and try again.")
    
    
    

print("\n" + "=" * 76)
print("Thank you for using LOGIN SIMULATOR!".center(76))
print("A Python CLI Project".center(76))
print("Developed by Harshit Pal | Python Learning Project".center(76))
print("Version: 1.0.0".center(76))
print("=" * 76)