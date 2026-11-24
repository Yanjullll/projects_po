weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

bmi = weight / (height ** 2)
print(f'--- Отчет о состоянии здоровья ---\n'
    f' Рост: \t {height} см'
    f' Вес: \t {weight} кг'
    f'Индекс массы тела: {bmi:.2f}')