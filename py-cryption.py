from cryptography.fernet import Fernet
import os
import requests

#Used for the password generator API, specifies the length of the password
length = '16' 
    
# Generate a key (keep this secret and store it securely)
def generate_key(key_name):
    key = Fernet.generate_key()
    with open(f"{key_name}.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load the key
def load_key(key_name):
    with open(f"{key_name}.key", "rb") as key_file:
        return key_file.read()
    
# Encrypt a file
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    
# Decrypt a file
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    
#Initial messages and options
print('Welcome To Py-Cryption, please select and option')
print('1 - password generator (generates strong 16 character password)')
print('2 - encryption center (you can use this to encrypt and decrypt files)')
choose = input('please select and option: ')

#This block of code is the password generator which will run if the user selects 1
if choose == '1':
    print('welcome to the password generator')
    print('here is your random password.')
    api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
    response = requests.get(api_url, headers={'X-Api-Key': 'IT1gf8xR5wt1BUonK7vmSQ==pWywC6sKvZIcYv1r'})
    if response.status_code == requests.codes.ok:
        print(response.text)

#This block of code is the encryption program
if choose == '2':
    print('Welcome to encryption! Please see below')
    print('This tool will encrypt a file and secure it using a key')
    print('The file can only be decrypted with the key it was encrypted with')
    print('Make sure to keep track of which files are encrypted with which keys')
          
    #Lets user choose between encyrption and decryption
    option = input('Type 1 for encryption, type 2 for decryption: ')
    file_path = input('Please input the path to your file including file name and extenstion: ') 

    if option == '1': #encrypts a file, and generates a key that can be named by the user
        key_name = input('Enter a name for the key without extension: ')
        key_file_name = f"{key_name}.key"
    
        if not os.path.exists(key_file_name): #creates a key with the name given by the user
            key = generate_key(key_name)
            print(f"New key '{key_file_name}' generated and saved.")
        else:
            key = load_key(key_name)
            print(f"Using existing key '{key_file_name}'.")
        
        encrypt_file(file_path, key) #encrypts the file
        print(f"File '{file_path}' encrypted using '{key_file_name}'.")

    elif option == '2': #decryption
        key_name = input('Enter the key name used for encryption without extenstion: ')
        key_file_name = f"{key_name}.key"
        
        if not os.path.exists(key_file_name): #loads the key
            print(f"Key file '{key_file_name}' not found! Cannot decrypt.")
        else:
            key = load_key(key_name)
            try:
                decrypt_file(file_path, key) #decrypts the file
                print(f"File '{file_path}' decrypted using '{key_file_name}'.")
            except Exception as e:
                print("Decryption failed:", e)

    else:
        print('Not a valid option.')

