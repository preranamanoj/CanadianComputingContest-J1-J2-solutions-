#special day = february 18
#Before - before Feb 18
#After - after Feb 18

month = int(input()) #enter the month
day = int(input()) #enter the day 
if month == 2 and day == 18:
  print("Special")
elif month < 2 and day <32:
  print("Before")
elif month == 2 and day <18:
  print("Before")
elif 13> month >= 2 and 32 > day: #12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 (month)
  print("After")                      
  
