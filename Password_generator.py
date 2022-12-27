### Password generator. ###

import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Generate a random Uppercase letter (based on ASCII code)
upcl1 = chr(random.randint(65,90))
upcl2 = chr(random.randint(65,90)) 
upcl3 = chr(random.randint(65,90)) 
upcl4 = chr(random.randint(65,90)) 
upcl5 = chr(random.randint(65,90)) 
upcl6 = chr(random.randint(65,90)) 


#Generate password using all the characters, in random order
password = upcl1 + upcl2 + upcl3 + upcl4 + upcl5 + upcl6
password = shuffle(password)

#Ouput
print(password)
