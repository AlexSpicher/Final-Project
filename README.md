# Final-Project Week 1
Encryption Program that uses a password generator API secure the file.

The code will most likely utalize this API for password generation: https://www.api-ninjas.com/api/passwordgenerator
- After encrypting files, a password will be required to decrypt. This API will provide users the option to generate a strong password.

How the code will work:
- Naviagte the command line interface of your choosing to the directory where the py file is located (This will most utalize the os library)
- Running the program will give users the option to either encrypt or decrypt.
- The program will prompt the user to pass the file path to the program
- If encryption is chosen, the Fernet library will be used to encrypt the file.
- Users will then choose a password to protect the file (Users can choose their own, or generate one with the password API)
- The file can be re-ran to decrypt the file (Users will be prompted for the password to decrypt after the path is specified).

Libraries Needed:
- cryptography (pip install cryptography)
- OS (pip install OS)

# Week-Two-Complete
This week I focused on getting the API to function properly. The block of code that utalizes the password API has been uploaded for viewing and testing, and will later be implemented into the full project.
The code on its own is pretty neat if you just want to mess around with it an generate some passwords. It can be ran on its own. 

# Week Three Complete
This week I completed the basic encryption and decryption functions. Next week will focus on the integration of the API as well as some minor tweaks and additions.
I also think I want to alter the code so that instead of encrypting the entire directory, you pass it a file path and are able to pick and choose which files you want encrypted.
