volume = float(input('Введите необходимый объем раствора (в мл): '))
NaCl_mass = volume*0.009

with open('recipe.txt', "w", encoding="utf-8") as table:
    table.write(f'ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\n'
                f'Общий объем: [{volume}] мл'
                f'Масса соли:  [{NaCl_mass:.2f}] г'
                f'Объем воды:  [{volume}] мл')
