# Secure Data Hiding in Image Using Steganography

This Python project demonstrates a simple implementation of Steganography, where secret messages are securely hidden in image files. Using basic image manipulation techniques, the secret message is embedded into the pixel values of an image, and a passcode is required for decryption. The message is not visible in the image, making this a useful method for covert communication.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Encrypting the Message](#A.-encrypting-the-message)
  - [Decrypting the Message](#B.-decrypting-the-message)
- [License](#license)
- [Author](#author)

## Introduction

This project enables you to hide a secret message inside an image file and retrieve it later using a passcode. The secret message is encoded by modifying the pixel values of the image. This method is simple yet effective for demonstrating the concept of steganography.

### Key Features:
- Encrypt a message into an image using a passcode.
- Retrieve the secret message using the correct passcode.
- Save and load encrypted data using `pickle`.
- The `os` module is used for file system operations, like opening the encrypted image after encryption.

## Getting Started

To use this project, follow these steps:

1. **Download the repository** or **clone it using Git**:
    ```bash
    git clone https://github.com/PrabjyotSingh2904/Secure-Data-Hiding-In-Image-Using-Steganography.git
    ```

2. Ensure you have the required dependencies (`OpenCV`, `pickle`, and `os`). Install OpenCV by running:
    ```bash
    pip install opencv-python
    ```

3. **Place your original image** (e.g., `Original_Image.jpg`) in the project directory.

## Project Structure

- `encrypt.py`: Script for encoding the secret message into the image.
- `decrypt.py`: Script for retrieving the secret message from the image.
- `data.pkl`: File that stores the passcode, character mapping, encrypted image, and secret message (used for decryption).

## Requirements

- Python 3.x
- OpenCV (`cv2`): Used for image manipulation.
- `pickle`: Used for saving encrypted data.
- `os`: Used for file handling tasks like opening the encrypted image after encryption.

## Usage

### A. Encrypting the Message (`encrypt.py`)

The process for encrypting the message into an image involves modifying the pixels of the image to store the message. Here's how it works:

#### Steps:
1. Prepare the image (`Original_Image.jpg`) that will be used to hide the secret message.
2. Run the encryption script: (`python encrypt.py`)
3. Enter the secret message when prompted. This is the message you want to hide inside the image.
4. Enter a passcode when prompted. This passcode will be used later for decryption.

#### Example:
```bash
(stegano_env) PS C:\Users\VICTUS\Desktop\AICTE INTERNSHIPS PRABJYOT\IBM skillsbuild internship\Stenography-main> python encrypt.py
Enter secret message: This is a secret message
Enter a passcode: pass2904
Image encrypted and saved as 'Encrypted_Image.jpg'
Encryption Successful
```

#### How It Works:

- The message is converted into ASCII values.
- These ASCII values are embedded into the RGB values of the image pixels. The pixel values are modified slightly to store one character at a time. The RGB channels (Red, Green, Blue) are cycled through to encode the message across multiple pixels.
- The passcode, character mappings, and the image data are saved to a file (`data.pkl`) for later use during decryption.

#### Output:
- `Encrypted_Image.jpg`: The image with the hidden message.
- `data.pkl`: File containing the passcode, the mapping for encoding/decoding, and the modified image data.


### B. Decrypting the Message (`decrypt.py`)

To retrieve the secret message, follow these steps:

#### Steps:
1. Ensure that `Encrypted_Image.jpg` and `data.pkl` are available in the same directory.
2. Run the decryption script:(`python decrypt.py`)
3. Enter the passcode you used during encryption when prompted.

#### Example:
```bash
(stegano_env) PS C:\Users\VICTUS\Desktop\AICTE INTERNSHIPS PRABJYOT\IBM skillsbuild internship\Stenography-main> python decrypt.py
Enter passcode for Decryption: pass2904
Decryption message: This is a secret message
```

#### How It Works:

- The encrypted image is loaded.
- The pixel values of the image are retrieved, and the encoded message is extracted using the character mappings saved during encryption.
- If the correct passcode is entered, the original message is displayed. If the passcode does not match, an error message will be shown.

#### Output:
- Displays the decrypted message if the correct passcode is entered.
- If the passcode is incorrect, an error message will appear:
    ```plaintext
    YOU ARE NOT AUTHORIZED
    ```


## License

This project is open-source and available under the MIT License.

## Author
PRABJYOT SINGH
