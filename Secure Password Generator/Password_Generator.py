# Import modules
import secrets
import string

# Function required to get users desired password length
def get_password_length():
    length = int(input("Enter desired password length: "))
    return length

# Function to build the unique password given user desired length
def randomize_password(length):
    print(f"Randomizing {length} character password...")
    print()
    # Builds a wordlist containing [a-zA-Z0-9] characters
    character_list = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # Selects a single character from the wordlist per password character length
    password = ''.join(secrets.choice(character_list) for character in range(length))
    return password

def main():
    while True:
        length = get_password_length()
        # Checks password length to ensure password complexity
        while length < 8:
            # If password length is less than 8 characters prompt again
            print("Password is too short, try again..")
            print()
            # Prompts for new password length
            length = get_password_length()

        # If password length is more than 8 characters don't prompt again
        print("Password length is valid..")
        print()
        # Stores the randomized password
        password = randomize_password(length)
        # Displays randomized password for user
        print(f"Your password: {password}")
        print()
        # Prompts if a new password should be created
        create_new_password = input("Create a new password (y/n)? ")
        print()
        # If input is 'n' break out of the loop
        if create_new_password.lower() == "n":
            print("Thanks for using the generator!")
            break
        # If input is 'y' continue with loop
        elif create_new_password.lower() == "y":
            continue
        # If input is not 'y/n' prompt user for input
        else:
            print("Please enter (y/n): ")

if __name__ == "__main__":
    main()