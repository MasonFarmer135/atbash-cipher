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
            break

        elif (userChoice == "DECODE" or userChoice == "D"):
            userMessage = input("Enter a message to decode: ")
            break

        else:
            userChoice = input('ERROR: Incorrect input. Please type "Encode" or "Decode": ')
            userChoice = userChoice.upper()

    return userChoice, userMessage

try:
    running = True
    welcomeMessage()

    while (running == True):
        userChoice, userMessage = userInput()

        if (userChoice == "ENCODE" or userChoice == "E"):
            print ("\n" + "Encode: " + userMessage + "\n")

        elif (userChoice == "DECODE" or userChoice == "D"):
            print ("\n" + "Decode: " + userMessage + "\n")

        restartApplication = input("Would you like to restart the application? ")
        restartApplication = restartApplication.upper()

        while True:
            if (restartApplication == "YES" or restartApplication == "Y"):
                break

            elif (restartApplication == "NO" or restartApplication == "N"):
                running = False
                break

            else:
                restartApplication = input('ERROR: Incorrect input. Please type "Yes" or "No": ')
                restartApplication = restartApplication.upper()

except KeyboardInterrupt:
    print ("\n" + "KEYBOARD INTERRUPT: Exiting the application.")