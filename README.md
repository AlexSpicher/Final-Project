# Final-Project
Encryption Program that uses a password generator API secure the file.

The code will most likely utalize this API for password generation: https://www.api-ninjas.com/api/passwordgenerator
- After encrypting files, a password will be required to decrypt. This API will provide users the option to generate a strong password.

How the code will work:
- Place the python file in the directory with the files you want encyrpted or decrypted. (This will most utalize the os library)
- Running the program will give users the option to either encrypt or decrypt.
- If encryption is chosen, the Fernet library will be used to encrypt the files.
- Users will then choose a password to protect the files (Users can choose their own, or generate one with the password API)
- The file can be re-ran to decrypt the files (Users will be prompted for the password to decrypt).

Libraries Needed:
- Fernet
- OS

#Week-Two-Complete
This week I focused on getting the API to function properly. The block of code that utalizes the password API has been uploaded for viewing and testing, and will later be implemented into the full project
