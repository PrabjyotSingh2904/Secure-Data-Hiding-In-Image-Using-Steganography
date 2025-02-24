import cv2
import pickle

# Load the variables from the file
with open('data.pkl', 'rb') as f:
    password, c,img, msg = pickle.load(f)

# Initialize the decrypted message as an empty string
message = ""

# Initialize indices for decoding the image pixels
n = 0   # Row index
m = 0   # Column index
z = 0   # Channel index (R, G, B)

# Prompt user for the passcode for decryption
pas = input("Enter passcode for Decryption : ")
if password == pas:    # Check if the entered passcode matches the saved passcode
    # Loop through each character in the encrypted message
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]    # Decode the character from the image pixel
        n = n + 1   # Move to the next row
        m = m + 1   # Move to the next column
        z = (z + 1) % 3   # Cycle through RGB channels
    print("Decryption message : ", message)   # Print the decrypted message
else:
    print("YOU ARE NOT AUTHORIZED")    # Print error message if passcode is incorrect
