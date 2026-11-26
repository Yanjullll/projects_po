protein_mass = float(input('Введите массу белков (г): '))
fats_mass = float(input('Введите массу жиров (г): '))
carbs_mass = float(input('Введите массу углеводов (г): '))

kcal = protein_mass*4 + fats_mass*9 + carbs_mass*4

print(f'Общая калорийность: {kcal}')