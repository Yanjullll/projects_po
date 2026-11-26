donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу реципиента (I, II, III, IV): ").strip().upper()
if donor == recipient or donor == 'I':
    print("Кровь донора подходит для переливания")
else:
    print("Кровь донора не подходит для переливания")
