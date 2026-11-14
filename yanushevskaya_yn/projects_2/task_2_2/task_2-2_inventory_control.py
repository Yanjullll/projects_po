reagent = input("Введите назвние реагента: ")
quantity = input("Введите количество реагента: ")
f = open("inventory.txt", "w", encoding="utf-8")

print(f'Реактив {reagent} поступил на склад в количестве {quantity} шт.', file=f)
f.close()