import random
class Generator:
    def __init__(self, length):
        self.length = length
        self.dictionary = 'abcdefghijklmnopqrstuvwxyz1234567890!@$%#&*()'

    def generate_password(self):
        password = ''
        for _ in range(self.length):
            letter = random.choice(self.dictionary)
            password += letter
        return password

    def print_password(self):
        print(f'Ваш пароль: {self.generate_password()}')

generator = Generator(int(input('Введите длину пароля: ')))
generator.print_password()

