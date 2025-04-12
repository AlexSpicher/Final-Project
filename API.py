'''
This week's iteration was getting the API working.
This block of code will be later integated with the encryption aspect
Alex Spicher
'''
import requests
length = '16'

print('You need to select a password to protect your files.')
print('press 1 below to choose your own password.')
print('press 2 below to generate a 16 character password from the API.')
option = input('input: ')

if option == '1':
    passw = input('type password here: ')
elif option == '2':
    print('here is your random password.')
    api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
    response = requests.get(api_url, headers={'X-Api-Key': 'IT1gf8xR5wt1BUonK7vmSQ==pWywC6sKvZIcYv1r'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)