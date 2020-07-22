# Lesson 5 - Short if statement syntax and pass statement
import datetime as dt

dayType = 3
weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass

dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescription)
print('weekend') if dayType == 1 else print('workday') if dayType == 2 else print('holiday')

# LAB

price = 123
bonus = 23
bonus_granted = False

if bonus_granted:
    price -= bonus
print(price)

# Short if
price = 123
bonus = 23
bonus_granted = True
price = price - bonus if bonus_granted else price
print(price)

# Normal if
rating = 3

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

# Short if
print('very good') if rating == 5 else print('good') if rating == 4 else print ('weak')

today_weekday = dt.date.today().strftime('%A')

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")

print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")
