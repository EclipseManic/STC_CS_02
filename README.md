## Image Encryption Tool
----------------------

This is a simple image encryption and decryption tool using basic pixel manipulation techniques. You can choose between two operations:
1. XOR Encryption
2. Pixel Swapping

## Developed by: EclipseManic

----------------------
## Features:
- Encrypts any RGB image using XOR or swapping pixels.
- Automatically saves the encryption key in a file.
- Can decrypt the image using the saved key file.
- Helps demonstrate how image data can be manipulated securely.

----------------------
## How to Use:

1. Run the script:
   python image_encryptor.py

2. Choose an option:
   - Enter '1' to encrypt an image
   - Enter '2' to decrypt an image

----------------------
## For Encryption:
- Enter the path to the image you want to encrypt.
- Choose the operation: 'xor' or 'swap'

Output:
- Encrypted image saved as: encrypted.png
- XOR key saved as: xor_key.txt (if you used XOR)
- Swap order saved as: swap_key.npy (if you used swap)

----------------------
## For Decryption:
- Enter the path to the encrypted image.
- Choose the correct operation used during encryption.
- Make sure the correct key file (xor_key.txt or swap_key.npy) is in the same folder.

Output:
- Decrypted image saved as: decrypted.png

----------------------
## Requirements:
- Python 3.x
- numpy
- pillow (PIL)

## Install using:
pip install numpy pillow

----------------------
## Note:
- Make sure to keep your key files safe. Without them, decryption will not work.
- Works only on RGB images.

----------------------
## Author:
EclipseManic
