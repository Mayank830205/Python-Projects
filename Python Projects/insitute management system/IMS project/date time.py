import datetime
x=datetime.datetime.now()
year=x.strftime("%Y")
month=x.strftime("%b")
day=x.strftime("%d")
print(day+"-"+month+"-"+year)