print("ASCII Value Checker")

while True:
    char = input("Enter a single character: ")
    if type(char) is str and len(char) == 1:
        ascii_val = ord(char)
        print("Character:", char)
        print("ASCII Value:", ascii_val)
        print("Character Type: ", end="")
        if ascii_val >= 65 and ascii_val <= 90:
            print("Uppercase Letter")
        elif ascii_val >= 97 and ascii_val <= 122:
            print("Lowercase Letter")
        elif ascii_val >= 48 and ascii_val <= 57:
            print("Number")
        elif ascii_val == 32:
            print("Space")
        else:
            print("Special Character")
    else:
        print("Error: Please choose only one character")