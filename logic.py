import random


def play_game(min_number, max_number, capital, attempts):
    secret_number = random.randint(min_number, max_number)

    while attempts > 0 and capital > 0:
        print(f"У вас осталось {attempts} попыток и {capital} капитала.")
        
        try:
            bid = int(input("Сколько вы хотите поставить? "))

            if bid > capital:
                print(f'Ставка не может быть больше {capital}.')
                continue

            guess_the_number = int(input(f"Угадай число в диапазоне от {min_number} до {max_number}: "))
        except ValueError:
            print("Пожалуйста, введите правильное число.")
            continue

        if guess_the_number == secret_number:
            print('Вы выиграли!!!!')
            winnings = bid * 2
            capital += winnings
        else:
            print("Вы проиграли")
            capital -= bid

        attempts -= 1

    if attempts == 0 and capital > 0:
        print(f"У вас осталось {capital} капитала.")
    elif capital == 0:
        print('У вас закончился капитал.')
