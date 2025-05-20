# Image Encryption Tool @Author :- EclipseManic

A simple Python tool for encrypting/decrypting images using pixel manipulation techniques.

## Features
- **Pixel Swapping**: Randomly shuffles pixel positions
- **XOR Operation**: Applies bitwise XOR transformation
- **Key Management**: Auto-saves encryption keys for decryption
- **Cross-Platform**: Works with JPEG, PNG, and other common image formats

## Requirements
- Python 3.x
- Pillow (PIL fork)
- numpy

Install dependencies:  
`pip install Pillow numpy`

## Usage

### Encryption
1. Run the program
2. Choose **1 (Encrypt)**
3. Enter image path
4. Select operation:
   - `swap`: Random pixel shuffling
   - `xor`: Value modification with numeric key
5. Encrypted image saved as `encrypted.png`
6. Key file created:
   - `swap_key.npy` for swap operations
   - `xor_key.txt` for XOR operations

### Decryption
1. Run the program
2. Choose **2 (Decrypt)**
3. Enter encrypted image path
4. Select same operation used for encryption
5. Ensure corresponding key file is present
6. Decrypted image saved as `decrypted.png`

## Example

```bash
# Encrypt with XOR
$ python image_crypto.py
Choose operation (1/2): 1
Enter image path: cat.jpg
Choose operation (swap/xor): xor
Enter numeric key (0-255): 189

# Decrypt XOR
$ python image_crypto.py  
Choose operation (1/2): 2
Enter encrypted image path: encrypted.png
Choose operation (swap/xor): xor
