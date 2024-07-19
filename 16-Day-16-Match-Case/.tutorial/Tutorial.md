# *Match Case Statements
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements. If this is your first language, dont worry as I will tell you everything you need to know about match case statements in this video!

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

1. The match keyword
2. One or more case clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.
## Syntax:
```python
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n
```
### Example:
```python
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
```
### Output:
```
x % 2 == 0 and case is 4
```

In the example you provided, you are using Python's `match` statement, introduced in Python 3.10, which allows for pattern matching. Here's an explanation of the different cases you have:

1. **Case with a specific value (0)**:
    ```python
    case 0:
        print("x is zero")
    ```
    This case checks if `x` is exactly 0. If `x` is 0, it will print "x is zero".

2. **Case with a specific value and an additional condition**:
    ```python
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    ```
    This case checks if `x` is 4 and if `x % 2 == 0`. Since `x` is 4 and 4 is even, it will print "x % 2 == 0 and case is 4".

3. **Empty case with an if-condition**:
    ```python
    case _ if x < 10:
        print("x is < 10")
    ```
    The `_` symbol is a wildcard that matches any value. The condition `if x < 10` adds an extra check. Since `x` is 4 and 4 is less than 10, it will print "x is < 10".

4. **Default case**:
    ```python
    case _:
        print(x)
    ```
    This is a default case that will match any value not matched by the previous cases. Since `x` is already matched by the third case, this default case will not execute in this example.

Putting it all together, for `x = 4`, the output of the script would be:

```
x % 2 == 0 and case is 4
x is < 10
```

Note that both the second and third cases are matched because they are not mutually exclusive. If you want only one case to execute, you would need to order the conditions more carefully or use a different control structure.
## [Next Lesson>>](https://github.com/Harshita1303/Python/blob/main/17-Day17-For-Loops/.tutorial/Tutorial.md)
