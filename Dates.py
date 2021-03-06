# A date is not a data type
# You have to import a module datetime to work with dates
import datetime
x = datetime.datetime.now()
print(x) # YYYY-MM-DD HH:MM:SS.MS

print(x.year)
print(x.strftime("%A"))

#creating date objects
x = datetime.datetime(2020, 5, 17)
print(x)

# strftime() Method
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# All format codes
print(x.strftime("%a")) #Weekday, short version "Wed"
print(x.strftime("%A")) #Weekday, full version "Wednesday"
print(x.strftime("%w")) #Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d")) #Day of month 01-31
print(x.strftime("%b")) #Month name, short version "Dec"
print(x.strftime("%B")) #Month name, full version "December"
print(x.strftime("%m")) #Month as a number 01-12
print(x.strftime("%y")) #Year, short version without century "18"
print(x.strftime("%Y")) #Year, full version "2018"
print(x.strftime("%H")) #Hour 00-23
print(x.strftime("%I")) #Hour 00-12
print(x.strftime("%p")) #AM/PM
print(x.strftime("%M")) #Minute 00-59
print(x.strftime("%S")) #Second 00-59
print(x.strftime("%f")) #Microsecond 000000-999999
print(x.strftime("%z")) #UTC offset "+0100"
print(x.strftime("%Z")) #Timezone "CST"
print(x.strftime("%j")) #Day number of year 001-366
print(x.strftime("%U")) #Week number of year, Sunday as first day of week "52"
print(x.strftime("%W")) #Week number of year, Monday as first day of week "52"
print(x.strftime("%c")) #Local version of date and time "Mon Dec 31 17:41:00 2018"
print(x.strftime("%x")) #Local version of date "12/31/18"
print(x.strftime("%X")) #Local version of time "17:41:00"
print(x.strftime("%%")) #A % character "%"
