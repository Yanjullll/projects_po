full_name = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Вывод: ")

with open("journal.txt", "w", encoding="utf-8") as file:
    # Записываем верхнюю границу рамки
    file.write("-" * 50 + "\n")
    file.write("| Электронный лабораторный журнал |\n")
    file.write("-" * 50 + "\n")
    file.write(f"| ФИО исследователя : {full_name} |\n")
    file.write(f"| Дата             : {date}         |\n")
    file.write(f"| Эксперимент      : {experiment_name} |\n")
    file.write("-" * 50 + "\n")
    file.write("| Вывод:                          |\n")

    # Вывод текста с переносом строки
    file.write(conclusion + "\n")

    # Можно добавить дополнительную строку с границей, если нужно
    # file.write("-" * 50 + "\n")