"""
author = Jana Sedlarikova
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

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

# prep
separator = '-' * 40

# user list
users, passwds = ['bob', 'ann', 'mike', 'liz'], ['123', 'pass123', 'password123', 'pass123']
user_list = {}
for i in range(len(users)):
    user_list[users[i]] = passwds[i]


# 1 welcome
print(separator)
print(f'Welcome to the app. Please log in:')


# 2 log in
user = input('USERNAME:')
passwd = input('PASSWORD:')


# 3 check log in
if user_list.get(user, "") != passwd:
    if user in list(user_list.keys()):
        print(f'Wrong password. Bye')
        exit()
    else:
        print(f'There is no such user registered. Bye')
        exit()


# 4 vyber text
print(separator)
print(f'We have 3 text to be analyzed')
invalid_number, attemps_left = True, 2
while invalid_number:
    text_number = int(input('Enter a number btw. 1 and 3 to select:'))
    if text_number in range(1, 4):
        invalid_number = False
    elif attemps_left > 0:
        print(f'Invalid entry. Try again. You have {attemps_left} attempts left')
        attemps_left += -1
    else:
        print(f'No attempt left. Bye')
        exit()


# 5 text analyzer
my_text = TEXTS[text_number - 1]
words = my_text.split()
words_stats, words_length = {}, {}
words_number_sum = 0

print(separator)
print(f'There are {len(words)} words in the selected text.')

while words:
    word = words.pop().strip(",.")
    words_length[len(word)] = words_length.get(len(word), 0) + 1
    if word.istitle():
        words_stats['title'] = words_stats.get('title', 0) + 1
    elif word.isupper():
        words_stats['upper'] = words_stats.get('upper', 0) + 1
    elif word.islower():
        words_stats['lower'] = words_stats.get('lower', 0) + 1
    elif word.isnumeric():
        words_stats['numeric'] = words_stats.get('numeric', 0) + 1
        words_number_sum += float(word)

print(f'There are {words_stats.get("title", 0)} titlecase words')
print(f'There are {words_stats.get("upper", 0)} uppercase words')
print(f'There are {words_stats.get("lower", 0)} lowercase words')
print(f'There are {words_stats.get("numeric", 0)} numeric strings')


# 6 print result on word length
print(separator)
for i in range(len(words_length)):
    number = words_length.get(sorted(words_length)[i])
    print(sorted(words_length)[i], "*"*number, number)


# 7 print number sum
print(separator)
print(f'If we summed all the numbers in this text we would get: {words_number_sum}')
print(separator)
