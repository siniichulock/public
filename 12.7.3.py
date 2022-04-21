money = int(input('Money = '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for percent in per_cent:
    deposit.append(money*per_cent[percent]/100)
print('Deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))