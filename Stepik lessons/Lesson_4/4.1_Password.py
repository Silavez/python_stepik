#Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят»

a, b = input(), input()
if a==b:
    print('Пароль принят')
else:
    print('Пароль не принят')
