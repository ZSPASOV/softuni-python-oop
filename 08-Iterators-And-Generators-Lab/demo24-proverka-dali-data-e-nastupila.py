import datetime


expected_date = datetime.datetime(year=2020, month=11, day=23, hour=13, minute=46)
executed = False


while True:
    now = datetime.datetime.now()
    if now >= expected_date and not executed:
        print('happened!')
        executed = True