while True:
    print("\nРасход(1)")
    print("Показать расходы(2)")
    print("Завершить(3)")

    choice = input("Выберите: ")

    if choice == "1":
        cat = input("Категория: ")
        summa = input("Сумма: ")
        desc = input("Описание: ")

        with open("my_expenses.txt", "a", encoding="utf-8") as f:
            f.write(f"{cat} - {summa} руб. - {desc}\n")
        print("Добавлено!")

    elif choice == "2":
        try:
            with open("my_expenses.txt", "r", encoding="utf-8") as f:
                print("\nМои расходы:")
                print(f.read())
        except:
            print("Нет расходов")

    elif choice == "3":
        break