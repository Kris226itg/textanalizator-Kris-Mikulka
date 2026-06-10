TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

import os
def clear():
    os.system("cls")

clear()


users = {"bob" : "123", "ann" : "pass123", "mike": "password123", "liz" : "pass123"}


username = input("username: ")
password = input("password: ")

print("----------------------------------------")

if not username in users:
    print("username doesnt exist")
    exit()

if password != users[username]:
    print(f"wrong password")
    exit()


print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print("----------------------------------------")
number = input(f"Pick a number from 1 to {len(TEXTS)}: ")
if not number.isdigit():
    print(f"You entered '{number}', you were supposed to enter a number")
    exit()

number = int(number)
if number < 1 or number > len(TEXTS):
    print(f"You are supposed to enter a number from 1 to {len(TEXTS)}, you entered '{number}'")
    exit()

usedText = TEXTS[number - 1]


usedText = usedText.replace("\n", " ")

wordList = []


currentWord = ''
for letter in usedText:
    if not letter == ' ':
        currentWord += letter
    else:
        wordList.append(currentWord)
        currentWord = ''

# aby tam bylo i poslední slovo
wordList.append(currentWord) 

print("----------------------------------------")

print(f"There are {len(wordList)} words in this text")

titlecase = 0

for word in wordList:
    if word[0].isupper() and not word.isupper():
        titlecase += 1

print(f"There are {titlecase} titlecase words in this text.")

uppercase = 0

for word in wordList:
    if word.isupper():
        uppercase += 1

print(f"There are {uppercase} uppercase words in this text.")

lowercase = 0

for word in wordList:
    if word.islower():
        lowercase += 1

print(f"There are {lowercase} lowercase words in this text.")

numericStrings = []

for word in wordList:
    if word.isdigit():
        numericStrings.append(int(word))

print(f"There are {len(numericStrings)} numeric strings words in this text.")
sum = 0
for number in numericStrings:
    sum += number
print(f"The sum of all the numbers is {sum}")
print("----------------------------------------")
print("LEN|  OCCURENCES   |NR")
print("----------------------------------------")
lengths = []
for word in wordList:
    lengths.append(len(word))
occurances = []
longestLength = 0
for length in lengths:
    if length > longestLength:
        longestLength = length
for i in range(longestLength + 1):
    occurances.append(0)
for number in lengths:
    occurances[number] += 1
for i in range(len(occurances)):
    if not i == 0:
        string = f"{i}: {occurances[i] * '*'}"
        for z in range(longestLength + 4 - occurances[i]):
            string += ' '
        if i < 10:
            string += ' '
        string += '|' + str(occurances[i])
        print(string)