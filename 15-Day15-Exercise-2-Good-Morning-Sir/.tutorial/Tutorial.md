# Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
```python
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
```

# Solution

```python
import time

hour = int(time.strftime('%H'))

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if (hour >= 0 and hour < 12):
  print("Good Morning Sir")
elif (hour >= 12 and hour < 16):
  print("Good Afternoon Sir")
else:
  print("Good Evening Sir")
```

## [Next Lesson>>](https://github.com/Harshita1303/Python-CodewithHarry/blob/main/16-Day-16-Match-Case/.tutorial/Tutorial.md)
