weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

bmi = weight / (height ** 2)
print(f'--- Отчет о состоянии здоровья ---\n'
    f' Рост: \t {height} см\ny7'
    f' Вес: \t {weight} кг\n8'
    f'Индекс массы тела: {bmi:.2f}')