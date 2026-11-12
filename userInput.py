def getIntegerInput(number, min_val, max_val):
    while True:
        user_input = input(number)
        if user_input.isdigit():
            choice = int(user_input)
            if choice >= min_val and choice <= max_val:
                return choice
            else:
                print(f"Please enter a valid choice.")
        else:
            print("Invalid. Please enter a number.")

def getStringInput(number):
    while True:
        text = input(number).strip()
        if len(text) > 0:
            return text
        print("Input cannot be empty.")
