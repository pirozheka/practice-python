class Word:
    def __init__(self, word):
        self.word = word

    # Метод для проверки, содержит ли слово определенную букву
    def contains_letter(self, letter):
        return letter in self.word

    # Метод для отображения текущего состояния слова с учетом угаданных букв
    def display_word(self, guesses):
        for letter in self.word:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

class Player:
    def __init__(self):
        self.guesses = set()

    def make_guess(self):
        while True:
            try:
                guess = input('Введите букву: ').lower()
                if len(guess) == 1 and guess.isalpha():
                    return guess
                else:
                    print('Ошибка! Введите одну букву.')
            except ValueError:
                print('Ошибка! Введите буквенный символ!')

class Game:
    def __init__(self, word):
        self.word = Word(word)
        self.guesses = set()
        self.max_attempts = 6  # Максимальное количество попыток
        self.attempts_left = self.max_attempts
        self.player = Player()

    def display_word(self):
        self.word.display_word(self.guesses)

    def make_guess(self):
        self.guesses.add(self.player.make_guess())

    def check_win(self):
        return set(self.word.word) == self.guesses

    def check_lose(self):
        return self.attempts_left <= 0

    def play(self):
        while not self.check_win() and not self.check_lose():
            self.display_word()
            self.make_guess()
            if self.guesses.intersection(set(self.word.word)) == set():
                self.attempts_left -= 1
            print(f"Осталось попыток: {self.attempts_left}")

        if self.check_win():
            print("Поздравляем, вы выиграли!")
        else:
            print(f"Игра окончена. Загаданное слово: {self.word.word}")

    def reset_game(self):
        self.guesses = set()
        self.attempts_left = self.max_attempts

game = Game('лодка')
game.play()