from datetime import datetime

# my_str = '23.12.2020'
# my_date = datetime.strftime(my_str, '%d.%m.%Y')
# cr_year = my_date.year
# cr_month = my_date.month


my_string = '23.12.2020'

# Create date object in given time format yyyy-mm-dd
my_date = datetime.strptime(my_string, "%d.%m.%Y")

print(my_date)
print('Type: ',type(my_date))