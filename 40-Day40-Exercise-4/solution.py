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
    
    
