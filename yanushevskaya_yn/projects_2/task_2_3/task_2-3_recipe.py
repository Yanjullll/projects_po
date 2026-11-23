nutrient_medium_name = input('Пожалуйста, введите название питательной среды: ')
agar_concentration = input('Пожалуйста, введите концентрацию агара (в процентах): ')
sterilization_temperature = input('Пожалуйста, введите температуру стерилизации (в градусах Цельсия): ')

with open("recipe.txt", "w", encoding="utf-8") as card:
    card.write(f"\t{nutrient_medium_name}\n\n"
                 f"Концентрация агара: {agar_concentration} %\n"
                 f"Температура стерилизации: {sterilization_temperature}°C\n")

print('Файл "recipe.txt" успешно сформирован!')