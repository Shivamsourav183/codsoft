import random

def generate_password(length, char_set):
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def password_generator():
    print('----------- Welcome to the Secure Password Generator -----------')

    char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ().,/?^@!$%&*0123456789'

    try:
        number = int(input('How many passwords would you like to generate? '))
        length = int(input('What should be the length of each password? '))

        if number <= 0 or length <= 0:
            print('Error: Both values should be positive integers.')
            return
        
        print('\nGenerated Passwords:')
        for _ in range(number):
            print(generate_password(length, char_set))

    except ValueError:
        print('Error: Please enter valid numbers for both the count and length.')

if __name__ == "__main__":
    password_generator()
