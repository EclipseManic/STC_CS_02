from PIL import Image
import numpy as np
import random

print("\n=== Image Encryption Tool ===")
print("1. Encrypt Image\n2. Decrypt Image")
choice = input("Choose operation (1/2): ")

if choice == '1':
    # Encryption Process
    img_path = input("Enter image path: ")
    operation = input("Choose operation (swap/xor): ").lower()
    
    try:
        img = Image.open(img_path).convert("RGB")
        pixels = np.array(img)
        h, w, c = pixels.shape
        
        flat = pixels.reshape(-1, 3)
        secret_data = None
        key_filename = ""

        if operation == 'swap':
            # Generate and save shuffle pattern
            shuffle_order = np.random.permutation(len(flat))
            flat = flat[shuffle_order]
            key_filename = "swap_key.npy"
            np.save(key_filename, shuffle_order)
            
        elif operation == 'xor':
            # Generate and save XOR key
            key = random.randint(0, 255)
            flat = np.bitwise_xor(flat, key)
            key_filename = "xor_key.txt"
            with open(key_filename, "w") as f:
                f.write(str(key))
                
        else:
            print("Invalid operation!")
            exit()
        
        Image.fromarray(flat.reshape(h, w, c)).save("encrypted.png")
        print(f"Image encrypted! Key saved to {key_filename}")

    except Exception as e:
        print(f"Error: {str(e)}")

elif choice == '2':
    # Decryption Process
    img_path = input("Enter encrypted image path: ")
    operation = input("Choose operation (swap/xor): ").lower()
    
    try:
        img = Image.open(img_path).convert("RGB")
        pixels = np.array(img)
        h, w, c = pixels.shape
        flat = pixels.reshape(-1, 3)

        if operation == 'swap':
            # Load shuffle pattern and reverse it
            try:
                shuffle_order = np.load("swap_key.npy")
                reverse_order = np.argsort(shuffle_order)  # Create reverse mapping
                flat = flat[reverse_order]
            except FileNotFoundError:
                print("Missing swap_key.npy file!")
                exit()
                
        elif operation == 'xor':
            # Load XOR key and re-apply
            try:
                with open("xor_key.txt") as f:
                    key = int(f.read())
                flat = np.bitwise_xor(flat, key)
            except FileNotFoundError:
                print("Missing xor_key.txt file!")
                exit()
                
        else:
            print("Invalid operation!")
            exit()
        
        Image.fromarray(flat.reshape(h, w, c)).save("decrypted.png")
        print("Image decrypted successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

else:
    print("Invalid choice!")