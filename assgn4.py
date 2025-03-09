# Function to find the starting and ending digits
def find_start_end_digits(strings):
    digits = [1,2,3,4,5,6,7]
    for s in strings:
        if s[0].isdigit() and s[-1].isdigit():
            digits.append((int(s[0]), int(s[-1])))
    return digits

# Function to reverse a list
def reverse_list(lst):
    return lst[::-1]

# Function to prompt for further options
def further_options(start_end_digits, reversed_digits):
    while True:
        option = input("Would you like to print the original list, print the reversed list, or end the program? (original/reversed/end): ").strip().lower()
        if option == 'original':
            print("Original list of starting and ending digits:", start_end_digits)
            break
        elif option == 'reversed':
            print("Reversed list of starting and ending digits:", reversed_digits)
            break
        elif option == 'end':
            print("Program ended.")
            break
        else:
            print("Invalid option. Please try again.")

# Prompt user to enter their own list of strings
def get_user_strings():
    user_strings = []
    while True:
        user_input = input("Enter a string (or type 'done' to finish): ").strip()
        if user_input.lower() == 'done':
            break
        user_strings.append(user_input)
    return user_strings

# Main function
def main():
    print("Welcome to the String Processor!")
    strings = get_user_strings()

    # Find starting and ending digits
    start_end_digits = find_start_end_digits(strings)

    # Prompt user to enter if they want to reverse the list
    reverse_option = input("Do you want to reverse the list? (yes/no): ").strip().lower()

    if reverse_option == 'yes':
        reversed_digits = reverse_list(start_end_digits)
        further_options(start_end_digits, reversed_digits)
    elif reverse_option == 'no':
        further_options(start_end_digits, [])
    else:
        print("Invalid option. Please try again.")

    print("Final list of starting and ending digits:", start_end_digits)

# Run the main function
if __name__ == "__main__":
    main()
