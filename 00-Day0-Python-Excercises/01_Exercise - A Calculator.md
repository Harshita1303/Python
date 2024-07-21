## Exercise 1 - Create a Calculator
Create a calculator capable of performing addition, subtraction, multiplication, division modulus, exponent and floor division operations on two numbers. Your program should format the output in a readable manner!
## Soltuion 
```python
#A calculator using match case statements
#Taking input from user
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

while(True):
  
  print("\nEnter the operation you want to perform", end="\n")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Modulus")
  print("6. Exponent")
  print("7. Floor Division")
  print("8. Exit", end="\n\n")

  choice = int(input("Enter the choice: "))

  match choice:
    case 1:
      print("Addition of two numbers is: ", a+b)
      
    case 2:
      print("Subtraction of two numbers is: ", a-b)
      
    case 3:
      print("Multiplication of two numbers is: ", a*b)
      
    case 4:
      if b != 0:
        print("Division of two numbers is: ", a/b)
      else:
        print("Division by zero is not possible")
        
    case 5:
      print("Modulus of two numbers is: ", a%b)
      
    case 6:
      print("Exponent of two numbers is: ", a**b)
      
    case 7:
      print("Floor Division of two numbers is: ", a//b)
      
    case 8:
      print("Thank you")
      exit()
      
    case _:
      print("Invalid choice")
```


