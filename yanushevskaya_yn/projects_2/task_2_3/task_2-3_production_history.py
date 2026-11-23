# 1. СБОР ДАННЫХ
# Функция input() всегда возвращает данные в виде строки (str)
product = input("Тип продукта (йогурт/кефир): ")
batch_id = input("Номер партии: ")

# 2. РАБОТА С ФАЙЛОМ
# Конструкция 'with' гарантирует, что файл закроется автоматически.
# "w" (write) — режим записи: файл перезаписывается.
# encoding="utf-8" — параметр для корректной кириллицы.
with open("production_history1.txt", "w", encoding="utf-8") as report:

    # 3. ЗАПИСЬ И ФОРМАТИРОВАНИЕ
    report.write(f"ОТЧЕТ ПРОИЗВОДСТВА\n")

    report.write(f"Продукт:\t{product}\n")
    report.write(f"Партия №:\t{batch_id}\n")