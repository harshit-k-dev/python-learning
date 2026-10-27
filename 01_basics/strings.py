# level 1
# exer1
name= 'Harshit'
print(name)

#  exer2
ms ='''
Name = Harshit
City = Orai
Favourite Programming Language = Python
'''
print(ms)
# exer3
word = 'COMPUTER'
print(word[0])
print(word[3])
print(word[-1])

# exer4
word = input('Enter your word: ')
print(len(word))

# exer5
language = "Python"
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])

# exer6
word = "PROGRAMMING"
print(word[:4])
print(word[8:11])
print(word[2:7])

# level2
# exer7
sentence = input('Enter a Sentence: ')
print(sentence.upper())
print(sentence.lower())

# exer8
text = '  Learn Python  '
print(text) #print original string 
print(text.strip())
print(text.rstrip(' '))

# exer9
sentence = 'I like Java. Java is useful.'
print(sentence.replace('Java','Python'))

# exer10
sentence = input("Write a sentence: ")
print(sentence.split())

# exer11
text = 'python is an interesting language'
print(text.capitalize())
print(text.title())

# exer12
str1 = 'PYTHON'
print(str1.center(20))

# exer13
text = 'banana'
print(text.count('a'))
print(text.count('an'))

# exer14
text = 'I am learning Python'
print(text.find('Python'))
print(text.index('Python'))

# level3
# exer15
text = "Python123"
text1 ="Python 123"
text2 ="Python@123"
print(text.isalnum())
print(text1.isalnum())
print(text2.isalnum())

# exer16
text = "Python"
text4 ='Python3'
text5 = 'Hello World'
print(text.isalpha())
print(text4.isalpha())
print(text5.isalpha())

# exer17
a = 'hello'
b = 'Hello'
c ='hello@123'
print(a.islower())
print(b.islower())
print(c.islower())

# exer18
text= 'Hello'
print(text.isprintable())
text = 'Hello\n'
print(text.isprintable)

# exer19
str1 = '     '
str2 = '        '
str3 = 'Hello Harshit'
print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

# exer20
text6 = 'Hello World'
text7 = "hello world"
text8 = "Hello world"
print(text6.istitle())
print(text7.istitle())
print(text8.istitle())

# exer21
v = 'PYTHON'
m = 'Python'
l = '123'
print(v.isupper())
print(m.isupper())
print(l.isupper())

# exer22
text = 'python_learning.py'
print(text.startswith('python'))
print(text.endswith('.py'))

# level4
# exer23
text = 'PyThOn Is FuN'
print(text.swapcase())

# exer24
word = input('Enter a Word:')
print(word.isalpha())
print(word.islower())
print(word.isupper())
print(word.istitle())

# exer25
sentence = input('Enter a sentence: ')
character = input('Enter a character to find: ')

position = sentence.find(character)
print(f"The first position of character '{character}' is: {position}")

# exer 26
sentence = input("Enter a Sentence: ")
words = sentence.replace(","," ").split()
print("Words in the sentence: ", words)

# exer27
username = input('Enter your USERNAME: ')
print(username.isalnum())

# exer28
sentence = input('Enter a sentence: ')
print("Length of Sentence: ", len(sentence))
print("Uppercase form of sentence: ", sentence.upper())
print("Lowercase form of sentence: ", sentence.lower())
print("Word count: ", len(sentence.split()))
print("NO. of occurence of 'a': ", sentence.count("a"))
print("starts with the or not: ", sentence.startswith("The"))

# /exer29
text = " pYTHON is FUN "
cleaned_result = text.strip().title()
print("Cleaned text:", cleaned_result)

# exer30
sentence = input("Enter a Sentence: ")
wordCount = sentence.split()
wc2= len(wordCount)
print(wordCount,wc2)

# exer31
sentence = input("Enter a Sentence: ")
searchWord = input("Type Search Word: ")
positionWord = sentence.find(searchWord)
noOfOccurence = sentence.count(searchWord)
print(f"First position of search word: {positionWord}\n")
print(f"Number of Occurence: {noOfOccurence}\n")
print("Sentence starts with Search Word: ", sentence.startswith(searchWord))
print("Sentence ends with Search Word: ", sentence.endswith(searchWord))

# exer32
string = input("Enter a STRING: ")
print("Entered String is alphabetic: ", string.isalpha())
print("Entered String is alphanumeric: ", string.isalnum())
print("Entered String is all lowercase: ", string.islower())
print("Entered String is all uppercase: ", string.isupper())
print("Entered String contains whitespace: ", string.isspace())

# exer33
user_sentence = input("Enter your Sentence: ")
sentenceLength = len(user_sentence)
sentenceCenter = user_sentence.center(30)
titleCase = user_sentence.title()
swapCase = user_sentence.swapcase()
splitWords = user_sentence.split()
printableSentence = user_sentence.isprintable()
print("Length of Sentence: ", sentenceLength)
print("\nSentence width 30: ", sentenceCenter)
print("\nSentence in Title Case: ", titleCase)
print("\nSwaped Sentence: ", swapCase)
print("\nSplitted Sentence: ", splitWords)
print("\nIs Your sentence Printable: ", printableSentence)