def welcomeMessage():
    print ("\n" + "Welcome to Atbash Cipher.")
    print ("This application allows users to encode or decode a message.")
    print ("The encode and decode functions both identify each letter within a message and then replaces it with the opposite value in the alphabet.")
    return 0

def userInput():
    userChoice = input("\n" + "Would you like to encode or decode a message? ")
    userChoice = userChoice.upper()

    while True:
        if (userChoice == "ENCODE" or userChoice == "E"):
            userMessage = input("Enter a message to encode: ")
            userMessage = userMessage.upper()
            break

        elif (userChoice == "DECODE" or userChoice == "D"):
            userMessage = input("Enter a message to decode: ")
            userMessage = userMessage.upper()
            break

        else:
            userChoice = input('ERROR: Incorrect input. Please type "Encode" or "Decode": ')
            userChoice = userChoice.upper()

    return userChoice, userMessage

def encodeMessage():
    for character in userMessage:
        if (character == " "):
            encodedMessage = encodedMessage + character

        elif (character.isdigit() == True):
            encodedMessage = encodedMessage + character

        elif (character == "¬" or character == "`" or character == "!" or character == '"' or character == "£" or character == "$" or character == "€" or character == "%" or character == "^" or character == "&" or character == "*" or character == "(" or character == ")" or character == "-" or character == "_" or character == "=" or character == "+" or character == "[" or character == "{" or character == "]" or character == "}" or character == ";" or character == ":" or character == "'" or character == "@" or character == "#" or character == "~" or character == "\\" or character == "|" or character == "," or character == "<" or character == "." or character == ">" or character == "/" or character == "?"):
            encodedMessage = encodedMessage + character

        else:
            for letter in alphabet:
                if (letter == character):
                    characterPosition = alphabet.index(letter)
                    encodedMessage = encodedMessage + oppositeAlphabet[characterPosition]

    return encodedMessage

def decodeMessage():
    for character in userMessage:
        if (character == " "):
            decodedMessage = decodedMessage + character

        elif (character.isdigit() == True):
            decodedMessage = decodedMessage + character

        elif (character == "¬" or character == "`" or character == "!" or character == '"' or character == "£" or character == "$" or character == "€" or character == "%" or character == "^" or character == "&" or character == "*" or character == "(" or character == ")" or character == "-" or character == "_" or character == "=" or character == "+" or character == "[" or character == "{" or character == "]" or character == "}" or character == ";" or character == ":" or character == "'" or character == "@" or character == "#" or character == "~" or character == "\\" or character == "|" or character == "," or character == "<" or character == "." or character == ">" or character == "/" or character == "?"):
            decodedMessage = decodedMessage + character

        else:
            for letter in alphabet:
                if (letter == character):
                    characterPosition = alphabet.index(letter)
                    decodedMessage = decodedMessage + oppositeAlphabet[characterPosition]

    return decodedMessage

try:
    running = True
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    oppositeAlphabet = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    encodedMessage = ""
    decodedMessage = ""

    welcomeMessage()

    while (running == True):
        userChoice, userMessage = userInput()

        if (userChoice == "ENCODE" or userChoice == "E"):
            encodedMessage = encodeMessage()
            print ("\n" + "Encoded message: " + encodedMessage + "\n")

        elif (userChoice == "DECODE" or userChoice == "D"):
            decodedMessage = decodeMessage()
            print ("\n" + "Decoded message: " + decodedMessage + "\n")

        restartApplication = input("Would you like to restart the application? ")
        restartApplication = restartApplication.upper()

        while True:
            if (restartApplication == "YES" or restartApplication == "Y"):
                print("Restarting the application.")
                encodedMessage = ""
                decodedMessage = ""
                break

            elif (restartApplication == "NO" or restartApplication == "N"):
                print("Exiting the application." + "\n")
                running = False
                break

            else:
                restartApplication = input('ERROR: Incorrect input. Please type "Yes" or "No": ')
                restartApplication = restartApplication.upper()

except KeyboardInterrupt:
    print ("\n" + "KEYBOARD INTERRUPT: Exiting the application.")