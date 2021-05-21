"""
import random

print("H A N G M A N\nThe game will be available soon.")

lista = ['python', 'java', 'kotlin', 'javascript']
palabra = random.choice(lista)
guion = "-" * len(str(palabra[3:]))
entrada = str(input("Guess the word " + palabra[:3] + guion + ": "))

r = "You survived!" if entrada in lista and entrada == palabra else "You are hanged!"
print(r)

states = ['Russia', 'USA', 'USA', 'Germany', 'Italy']
print(set(states))  # {'Russia', 'USA', 'Italy', 'Germany'}

set1 = {'A', 'B', 'C'}
set2 = {'B', 'C', 'A'}
print(set1 == set2)  # True

nums = {1, 2, 2, 3}
print(1 in nums, 3 not in nums)  # True False

# mystery_set has been defined
string = input()
# delete string from mystery_set
if string in mystery_set:
    mystery_set.discard(string)


============================

numbers = input().split()
answers = input().split()

set1 = set(numbers)
set2 = set(answers)

if set1 == set2:
    print(True)
else:
    print(False)


===================================
import random

print("H A N G M A N\nThe game will be available soon.")
lista = ['python', 'java', 'kotlin', 'javascript']
palabra = random.choice(lista)
guion = "-" * len(str(palabra[:]))
print(guion)
entrada = str(input("Guess the word " + palabra[:3] + guion[3:] + ": "))

r = "You survived!" if entrada in lista and entrada == palabra else "You are hanged!"
print(r)

"""

import random

print("H A N G M A N\n")
lista = ['python', 'java', 'kotlin', 'javascript']
palabra = random.choice(lista)
set_palabra = set(palabra)
guion = "-" * len(str(palabra[:]))
guion2 = len(str(palabra[:]))

print(guion)
entrada = str(input("Input a letter: "))
set_entrada = set(entrada)

if entrada in set_palabra:
    print("\n", entrada)
    print(guion)
    print(palabra.replace('-', '{}').format(entrada))
    print(palabra.replace('-', '{}').format(guion2))
    print(guion2)




r = "You survived!" if entrada in lista and entrada == palabra else "You are hanged!"
print(r)
