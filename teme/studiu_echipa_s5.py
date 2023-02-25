# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex 1.Funcție care să afișeze data și ora curentă din România.
# (bonus: afișazăi și data și ora curentă din China)

import datetime


def time_ro():
    d0 = datetime.datetime.now()
    return f"{d0.strftime('%d')}-{d0.strftime('%m')}-{d0.strftime('%Y')} -> {d0.strftime('%X')}"


print(f"Ora in Romania: {time_ro()}")

# (bonus: afișează și data și ora curentă din China)
import pytz as pytz

tz = pytz.timezone("Asia/Shanghai")
ct = datetime.datetime.now(tz=tz)


def time_china():
    d0 = datetime.datetime.now()
    new_timezone = tz
    return f"China current time: {ct}"
    # return f"{new_timezone.strftime('%d')}-{new_timezone.strftime('%m')}-{new_timezone.strftime('%Y')} -> {new_timezone.strftime('%X')}"


print(time_china())

'''
from datetime import datetime, timedelta, timezone

# v1
def display_date_time_v1():       
    now = datetime.now()
    print(f"Date and time Romania: {now}")
    print(f"Date and time China: {now + timedelta(hours=5)}") 
    
display_date_time_v1()


# v2
import pytz  
def display_date_time_v2():
    timezone_ro = pytz.timezone('Europe/Bucharest')  # pt v2, trebuie stiute timezone-uri sau aflate (print(pytz.all_timezones)) 
    now = datetime.now(timezone_ro)
    print(f"Date and time Romania: {now}")

    timezone_cn = pytz.timezone('Asia/Hong_Kong') 
    now = datetime.now(timezone_cn)
    print(f"Date and time China: {now}")
    
display_date_time_v2()
'''


# Ex 2. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)

def christmas():
    # d0 = datetime.datetime(2023, 2, 9)
    d0 = datetime.datetime.now()
    d1 = datetime.datetime(2023, 12, 25)
    return (d1 - d0).days


print(f"Days from now until Chritsmas -> {christmas()}")

'''
from datetime import datetime

def days_til_birthday(birthday_date="25.12.2022"):
    birthday_date = datetime.strptime(s, "%d.%m.%Y")
    today = datetime.today()
    
    days_left = (birthday_date - today).days
    print(days_left)

days_til_birthday()

'''
