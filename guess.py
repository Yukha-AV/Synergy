import random


class RandomNumberGame:
    def __init__(self, _min, _max):
        self.victory = False
        self.min_val = _min
        self.max_val = _max
        self.exact_val = random.randint(_min, _max)
        self.closest_val = self.exact_val
        self.attempts_left = 10
        self.user_needs_help = 3

    def validate_input(self, s):
        if self.game_over():
            print("Игра окончена")
            return False
        try:
            i = int(s)
        except ValueError:
            print("Ошибка ввода, необходимо целое число в цифровом ввиде")
            return False
        if i < self.min_val or i > self.max_val:
            print("Ошибка ввода, загадано число от", self.min_val, "до", self.max_val)
            return False

        return True

    def print_rules(self):
        print("Загадано целое число от", self.min_val, "до", self.max_val, "включительно."
              "У вас", self.attempts_left, "попыток, что бы угадать это число. Удачи!")

    def guess(self, val):
        if val == self.exact_val:
            print("Поздавляем, Вы победили!")
            self.victory = True

        if val > self.exact_val:
            print("Загаданное число меньше этого числа")
        if val < self.exact_val:
            print("Загаданное число больше этого числа")

        self.attempts_left = self.attempts_left - 1

        if self.attempts_left != 0:
            print("Осталось попыток:", self.attempts_left)
        elif not self.victory:
            print("К сожалению, Вы проиграли :(")
            print("Было загадано число:", self.exact_val)

        if abs(val - self.exact_val) < abs(self.closest_val - self.exact_val) or self.closest_val == self.exact_val:
            self.closest_val = val

        if self.attempts_left <= self.user_needs_help and not self.closest_val == self.exact_val:
            print("Лучшая попытка:", self.closest_val)

    def game_over(self):
        return self.victory or self.attempts_left == 0


if __name__ == '__main__':
    play = True
    while play:
        game = RandomNumberGame(1, 100)
        game.print_rules()

        while not game.game_over():
            inp = input("Введите число:")
            if game.validate_input(inp):
                num = int(inp)
                game.guess(num)

        rep = input("Введите слово 'повторить', что бы повторить игру\n")
        if rep.lower() != "повторить":
            play = False
