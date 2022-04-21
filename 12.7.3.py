money = int(input('Money = '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
percent = list(map(float, per_cent.values()))
deposit = [money*percent[0]/100, money*percent[1]/100, money*percent[2]/100, money*percent[3]/100]
deposit = list(map(int, deposit))
print('Deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))