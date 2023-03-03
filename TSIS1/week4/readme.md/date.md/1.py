import datetime

def Data():
    x = datetime.date.today()
    y = datetime.timedelta(days=5)
    z = x-y
    return z
print(Data())