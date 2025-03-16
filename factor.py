import math


def validate_input(s):
    try:
        i = int(s)
    except ValueError:
        print("Ошибка ввода, необходимо целое число в цифровом ввиде")
        return False
    if not i > 0:
        print("Ошибка ввода, необходимо целое положительное число")
        return False

    return True


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


if __name__ == '__main__':
    inp = input("Введите число для вычисления факториала:")
    num_attempts = 5

    while num_attempts > 0:
        if validate_input(inp):
            num = int(inp)
            print("Значение факториала (n!):", factorial(num))
            print("Значение math.factorial():", math.factorial(num))
            break
        else:
            inp = input("Введите число для вычисления факториала"
                        " (число должно быть целым и положительным, например '5'):")
            num_attempts = num_attempts - 1
