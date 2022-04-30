ticket = int(input('Введите количество билетов: '))
price1, price2 = 990, 1390
total = 0
for i in range(ticket):
    age = int(input('Введите возраст посетителя: '))
    if 18 <= age < 25:
        total += price1
    elif age >= 25:
        total += price2
if ticket > 3:
    print('Вы получаете скидку 10%')
    total = int(total * 0.9)
print('Общая стоимость билетов:', total, 'руб.')
