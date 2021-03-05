# Write a Python program to calculate the length of a string.

def stringLength(str):
    i = 0
    for c in str:
        i += 1
    return i

print('stringLength(\'Andrew\') = ' + str(stringLength('Andrew')))

# Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String

def midString(str):
    mid = int (len(str)/2)
    return str[mid-1:mid+2]

print('midString(\'JhonDipPeta\') = ' + midString('JhonDipPeta'))

# Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1

def stringception(str1, str2):
    mid = int(len(str1)/2)
    return str1[:mid] + str2 + str1[mid:]

print('stringception(\'Ault\',\'Kelly\') = ' + stringception('Ault','Kelly'))

# Arrange string characters such that lowercase letters should come first

def rearrange(str):
    lowercase = []
    uppercase = []
    for c in str:
        if c.islower():
            lowercase.append(c)
        else:
            uppercase.append(c)
    return ''.join(lowercase + uppercase)

print('rearrange(\'PyNaTive\') = ' + rearrange('PyNaTive'))

# Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters

def strAverage(str1):
    strList = str1.split()
    sum = 0
    count = 0
    avg = 0
    for x in strList:
        if x.isnumeric():
            sum += float(x)
            count +=1
    avg = sum/count
    str2 = 'Sum : {}\nAverage : {}'
    print(str(str2.format(sum,avg)))

strAverage('English = 78 Science = 83 Math = 68 History = 65')

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

def swap2(str1,str2):
    return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
print(swap2('abc','xyz'))

# Find the last position of a substring “Emma” in a given string

def findLast(str1, str2):
    return str1.rfind(str2)

print(findLast("Emma is a data scientist who knows Python. Emma works at google.", 'Emma'))

# Write a Python program to remove the characters which have odd index values of a given string

def noOddIndex(str1):
    onlyEven = []
    for i in range(0,len(str1),2):
        onlyEven.append(str1[i])
    print(*onlyEven)

noOddIndex("Emma is a data scientist who knows Python. Emma works at google.")

# Remove special symbols/Punctuation from a given string

def noSymbols(str1):
    newStr = []
    for c in str1:
        if c.isalpha() or c.isspace():
            newStr.append(c)
    print(''.join(newStr))

noSymbols("/*Jon is @developer & musician")

# Removal all the characters other than integers from a string

def noChars(str1):
    oldStr = str1.split()
    newStr = []
    for word in oldStr:
        if word.isdigit():
            newStr.append(word)
    print (''.join(newStr))

noChars("I am 25 years and 10 months old")