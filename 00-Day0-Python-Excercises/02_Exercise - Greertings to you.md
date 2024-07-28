# Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. 
# Solution
We are going to use "time module" to create a program which greets you

```python
import time

#Current time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

#take hour using time module
hour = int(time.strftime('%H'))
print(hour)

if (hour >= 0 and hour < 12):
  print("Good Morning Sir")
elif (hour >= 12 and hour < 16):
  print("Good Afternoon Sir")
else:
  print("Good Evening Sir")
```

