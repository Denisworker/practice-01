# Практическая работа 2. Вариант 2. Конвертер единиц

work = True

while work:
    print()
    print("Выберите конвертер:")
    print("1. Градус Цельсия -> Градус Фаренгейта")
    print("2. Километры -> Мили")
    print("3. Килограммы -> Фунты")
    print("4. Метры -> Футы")
    print("5. Литры -> Галлоны")
    print("6. Мегабайты -> Гигабайты")
    print("7. Часы -> Минуты")
    print("8. Сантиметры -> Дюймы")

    choice = input("Ваш выбор: ")

    if choice == "1":
        try:
            c = float(input("Введите температуру: "))
            f = c * 9 / 5 + 32
            print(c, "C =", round(f, 2), "F")
        except ValueError:
            print("Ошибка: нужно ввести число")

    elif choice == "2":
        try:
            km = float(input("Введите километры: "))
            miles = km * 0.621371
            print(km, "км =", round(miles, 2), "миль")
        except ValueError:
            print("Ошибка: нужно ввести число")

    elif choice == "3":
        try:
            kg = float(input("Введите килограммы: "))
            pounds = kg * 2.20462
            print(kg, "кг =", round(pounds, 2), "фунтов")
        except ValueError:
            print("Ошибка: нужно ввести число")

    elif choice == "4":
        try:
            m = float(input("Введите метры: "))
            feet = m * 3.28084
            print(m, "м =", round(feet, 2), "футов")
        except ValueError:
            print("Ошибка: нужно ввести число")

    elif choice == "5":
        try:
            liters = float(input("Введите литры: "))
            gallons = liters * 0.264172
            print(liters, "л =", round(gallons, 2), "галлонов")
        except ValueError:
            print("Ошибка: нужно ввести число")

    elif choice == "6":
        try:
            mb = float(input("Введите мегабайты: "))
            gb = mb / 1024
            print(mb, "МБ =", round(gb, 2), "ГБ")
        except ValueError:
            print("Ошибка: нужно ввести число")

    elif choice == "7":
        try:
            hours = float(input("Введите часы: "))
            minutes = hours * 60
            print(hours, "ч =", round(minutes, 2), "мин")
        except ValueError:
            print("Ошибка: нужно ввести число")

    elif choice == "8":
        try:
            cm = float(input("Введите сантиметры: "))
            inches = cm / 2.54
            print(cm, "см =", round(inches, 2), "дюймов")
        except ValueError:
            print("Ошибка: нужно ввести число")

    else:
        print("Ошибка: такого конвертера нет")

    answer = input("Выполнить ещё одно преобразование? (да/нет): ")
    while answer != "да" and answer != "нет":
        print("Ошибка: введите да или нет")
        answer = input("Выполнить ещё одно преобразование? (да/нет): ")

    if answer == "нет":
        work = False

print("Работа программы завершена.")