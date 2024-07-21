# Excercise 04: Secret Code Language - code/decode 
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end
now append three random characters at the starting and the end
else:
simply reverse the string

## Decoding:
if the word contains less than 3 characters, reverse it
else:
remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

### Your program should ask whether you want to code or decode

```python
#Secret Code Language - code/decode

#take input from user
message = input("Enter the message:")
while(True):
  #Enter a choice from the user
  print("\nEnter the operation to be performed:\n1.Encode\n2.Decode\n3.Exit")
  choice = int(input("Enter your choice:"))

  #code the message
  def encode(message):
    ciphers = []
    words = 0
    
    #split the message into words
    words = message.split(' ')
  
    for i in words:
      if len(i) < 3:
        rev = i[::-1]
        ciphers.append(rev)
      else:
        a = 'abc'
        b = 'xyz'
        c = i[1:]
        d = i[0]
        code = a + c + d + b
        ciphers.append(code)
  
    return ciphers
  
  #decode the ciphers
  def decode(cipherText):
    text = []
  
    for i in cipherText:
      if len(i) < 3:
        rev = i[::-1]
        text.append(rev)
      else:
          c = i[3:-4]
          d = i[-4]
          decode = d + c
          text.append(decode)
    return text
  
  if (choice == 1):
    cipherText = encode(message)
    print("\nAfter encoding: ", cipherText)
    
  elif (choice == 2):
    finalMessage = decode(encode(message))
    print("\nAfter decoding: ", finalMessage)
    
  elif (choice == 3):
    print('Thank you for using our program')
    exit()
    
  else:
    print("Invalid choice!, try again")
```
## [Next Lesson>>](https://github.com/Harshita1303/Python-CodewithHarry/blob/main/41-Day41-Short-Hand-if-else/.tutorial/Tutorial.md)
