imya = input('Введите имя: ')
vozr = int(input('Введите возраст: '))
nom = input('Введите номер школы: ')
clas = int(input('Введите класс: '))

god = 2024 - (vozr - (7 + clas))

print(f'''
Привет, {imya}!

Поздравляю с окончанием {clas} класса школы №{nom} в {god} году.''')
