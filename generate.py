import random


def generator_email():
    login = ''
    for _ in range(10):
        login += random.choice('1234567890qwertyuioplkjhgfdsazxcvbnm')
    domain = random.choice(['gmail.com', 'rambler.ru', 'yandex.ru'])
    email = f'{login}@{domain}'
    return email

def generator_password():
    characters = '1234567890asddfghjklzxcvbnmqwertyuiopASDFGHJKLQWERTYUIOPZXCVBNM'
    length = random.randint(6, 12)
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password
