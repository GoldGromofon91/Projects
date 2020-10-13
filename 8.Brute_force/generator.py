import random


class GeneratorPassword:
    letters_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits_alphabet = '0123456789'
    symbols_alphabet = '.,/?!@#$%^&*():;\'"|\\'

    def __init__(self, pass_lenght=16, use_letters=True, use_digits=True, use_symbol=False):
        self.pass_lenght = pass_lenght
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_symbol = use_symbol

    def generate(self):
        alpha_str = ''
        password_str = ''
        if self.use_letters:
            alpha_str += self.letters_alphabet
        if self.use_digits:
            alpha_str += self.digits_alphabet
        if self.use_symbol:
            alpha_str += self.symbols_alphabet

        for i in range(self.pass_lenght):
            password_str += random.choice(alpha_str)

        return password_str


pswd_1 = GeneratorPassword(16, True, True, True)
user_pass = pswd_1.generate()
print(user_pass)
