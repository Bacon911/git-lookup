def checker(year):
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'Высокосный'
    else:
        return 'Не высокосный'

print(checker(input('Введите год: ')))