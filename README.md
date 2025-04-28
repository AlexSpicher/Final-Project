# Py-protection
Cyber protection program that can assist users in protecting their files and information
Generates strong passwords for users with the use of the password API, as well as encrypting and decrypting files using the cryptography library

# How the code will work:
- Naviagte the command line interface of your choosing to the directory where the py file is located, then run the program using python3 'py-protection.py' (Make sure you have python installed as well as the required libraries, python can be found here: https://www.python.org/downloads/windows/)
- Running the program will display some welcome and instructional messages before giving users the option to generate a password, or use the encryption tool
- Selecting password generation will display a strong 16 character password that can be copy and pasted at the users convencience.
- If encryption is chosen, welcome messages will be displayed and users will be given an option to encrypt or decrypt.
- Users will then be prompted to give the path of the file they wish to use (MAKE SURE TO INCLUDE THE FILE ISTELF IN THE PATH AS WELL AS THE EXTENSION .txt, .img, etc)
- The program will then ask users to name the key that will be used to encrypt the file. The file is then encrypted and the key is written to the directory the program is located in as a .KEY file.
- If decryption is chosen, the program will ask the user for the name of the key file used to encrypt the file (MAKE SURE TO KEEP TRACK OF YOUR KEYS)
- When decrypting, make sure you place the key to be used in the directory the program is running in. 
- The key is then used to decrypt the file
  
# Libraries Needed:
- cryptography (pip install cryptography)
- OS (pip install OS)
- requests (pip install requests)

# Week-Two-Complete
This week I focused on getting the API to function properly. The block of code that utalizes the password API has been uploaded for viewing and testing, and will later be implemented into the full project.
The code on its own is pretty neat if you just want to mess around with it an generate some passwords. It can be ran on its own. 

# Week Three Complete
This week I completed the basic encryption and decryption functions. Next week will focus on the integration of the API as well as some minor tweaks and additions.
I also think I want to alter the code so that instead of encrypting the entire directory, you pass it a file path and are able to pick and choose which files you want encrypted.

# Week Four Complete
This week was the final iteration for the project. The code file has been uploaded for usage. Please read the information above for instructions on how to use. I have updated the Initial readme to be consistent with how the code works. I deleted the files from week three because they were unecessary and I do not want users to get confused. They were simply smaller blocks of code from the main program anyway, so there isn't much to be missed (Also for some reason windows defender was flagging the encryption file as a virus, so theres that as well). 
