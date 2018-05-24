from datetime import datetime, timedelta

yesterday = datetime.today() - timedelta(days = 1)

print('Вчера было', str(yesterday.day) + '.' + str(yesterday.month) + '.' + str(yesterday.year) )

print('А сегодня', str(datetime.today().day) + '.' + str(datetime.today().month) + '.' + str(datetime.today().year) )

print('Ну а месяц назад', str(datetime.today().day) + '.' + str(datetime.today().month - 1 ) + '.' + str(datetime.today().year) )
