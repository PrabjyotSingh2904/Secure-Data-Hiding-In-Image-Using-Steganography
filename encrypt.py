import cv2
import os
import pickle

# Load the image
img = cv2.imread("Original_Image.jpg")  

# Prompt user for the secret message and passcode
msg = input("Enter secret message : ")
password = input("Enter a passcode : ")

# Initialize dictionaries for encoding and decoding characters
d = {}
c = {}

# Populate dictionaries with ASCII values and corresponding characters
for i in range(255):
    d[chr(i)] = i    # Character to ASCII mapping
    c[i] = chr(i)    # ASCII to character mapping

# Initialize indices for modifying image pixels
m = 0  # Column index
n = 0  # Row index
z = 0  # Channel index (R, G, B)

# Loop through each character in the secret message
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]    # Encode the character into the image pixel
    n = n + 1     # Move to the next row
    m = m + 1     # Move to the next column
    z = (z + 1) % 3    # Cycle through RGB channels

# Save the modified image
cv2.imwrite("Encrypted_Image.jpg", img)
os.system("start Encrypted_Image.jpg")  # Open the encrypted image
print(f"Image encrypted and saved as 'Encrypted_Image.jpg'")

# Save the passcode, character dictionary, modified image, and secret message to a file
with open('data.pkl', 'wb') as f:                       
    pickle.dump((password, c,img, msg), f)

print("Encryption Successful")