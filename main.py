def welcomeMessage():
    print ("\n" + "Welcome to Atbash Cipher.")
    print ("This application allows users to encode or decode a message.")
    print ("The encode and decode functions both identify each letter within a message and then replaces it with the opposite value in the alphabet." + "\n")
    return 0

try:
    welcomeMessage()

except KeyboardInterrupt:
    print ("\n" + "KEYBOARD INTERRUPT: Exiting the application.")