import datetime

year = input("태어난 해는 언제 인가요?")
year = int(year)

month = input("태어난 달은 언제 인가요?")
month = int(month)

day = input("태어난 날은 언제 인가요?")
day = int(day)

bday = datetime.datetime(year, month, day)

if bday.weekday() == 6:
    print("태어난 날은 일요일 이군요.")

if bday.weekday() == 0:
    print("태어난 날은 월요일 이군요.")

if bday.weekday() == 1:
    print("태어난 날은 화요일 이군요.")

if bday.weekday() == 2:
    print("태어난 날은 수요일 이군요.")

if bday.weekday() == 3:
    print("태어난 날은 목요일 이군요.")

if bday.weekday() == 4:
    print("태어난 날은 금요일 이군요.")

if bday.weekday() == 5:
    print("태어난 날은 토요일 이군요.")