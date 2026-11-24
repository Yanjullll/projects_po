protein_mass = float(input('Введите Массу белков (г): '))
fats_mass = float(input('Введите Массу жиров (г): '))
carbs_mass = float(input('Введите Массу углеводов (г): '))

kcal = protein_mass*4 + fats_mass*9 + carbs_mass*4

print(f'Общая калорийность: {kcal}')