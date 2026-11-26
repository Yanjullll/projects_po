quantity = int(input('Введите общее количество произведенных капсул (шт): '))
capacity = int(input('Введите количество капсул в одной упаковке (шт): '))

full_packages = quantity // capacity
remainder = quantity % capacity

print(f'--- Отчет фасовочного цеха ---\n'
    f'Полных упаковок: {full_packages}\n'
    f'Остаток капсул: {remainder}')