def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  year_value=is_leap(year)
  if year_value==True:
    month_days[1]+=1
  return month_days[month-1]
year = int(input("enter year:")) # Enter a year
month = int(input("enter month:")) # Enter a month
days = days_in_month(year, month)
print(days)
