import random
import string

j=5

NewArray = [j]

for i in range(j):
    NewArray.append(random.choice(string.ascii_uppercase))

print(NewArray)

