answer = int(input("Введите ответ Оли: "))

if answer <= 0:
    print("неверно")
else:
    n = answer
    is_power_of_two = True

    while n > 1:
        if n % 2 != 0:
            is_power_of_two = False
            break
        n //= 2

    if is_power_of_two:
        print("верно")
    else:
        print("неверно")


