# Snake Water Gun
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.
Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
# Solution
```python
'''SNAKE WATER GUN GAME
Rules: the gun beats the snake ,
the water beats the gun, 
and the snake beats the water.'''

#Greetings to the players
print("welcome to the \"snake-water-gun\" game")
print('Who score the most points wins the game')

#iniatilizing the variables
rahul_count = 0
kaveri_count = 0

#looping the game for 5 rounds
for game in range(5):

  #options to choose from
  print('\nChoose the input from the given options')
  print("1.snake\n2.water\n3.gun\n")

  #take input from players
  rahul = input("Rahul: ")
  kaveri = input("Kaveri: ")

  #if both the players choose the same option  
  if rahul == kaveri:
    print("\nDraw Match\n")
    
  #if rahul chooses snake and kaveri chooses water 
  elif (rahul == 'snake' and kaveri == 'water'):
    print('\nRahul wins\n')
    rahul_count += 1
    
  #if rahul chooses snake and kaveri chooses gun 
  elif (rahul == 'snake' and kaveri == 'gun') :
    print('\nkaveri wins\n')
    kaveri_count += 1
    
  #if rahul chooses water and kaveri chooses snake 
  elif (rahul == 'water' and kaveri == 'snake'):
    print('\nkaveri wins\n')
    kaveri_count += 1

  #if rahul chooses waater and kaveri chooses gun 
  elif (rahul == 'water' and kaveri == 'gun'):
    print('\nRahul wins\n')
    rahul_count += 1  
    
   #if rahul chooses gun and kaveri chooses snake 
  elif (rahul == 'gun' and kaveri == 'snake'):
    print('\nRahul wins\n')
    rahul_count += 1
    
  #if rahul chooses gun and kaveri chooses water 
  elif (rahul == 'gun' and kaveri == 'water'):
    print('\nkaveri wins\n')
    kaveri_count += 1

  else: 
    #if user enters invalid input
    print('\ninvalid input, try again')

#check the counts and declare the winner
if rahul_count > kaveri_count:
  print('\"Rahul wins the game\"')
elif rahul_count < kaveri_count:
  print('\"kaveri wins the game\"')
else:
  print('\"Draw Match\"')

```


