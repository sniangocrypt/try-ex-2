while True:
    try:
        num = int(input("Введите число: "))
        print(num)
        break
    except ValueError:
        print("Ошибка: введённое значение не является числом. Попробуйте ещё раз.")
