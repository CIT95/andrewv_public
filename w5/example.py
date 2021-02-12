from abc import abstractproperty


lst = []

while True:
    number = int(input('Enter a number'))
    if number < 0:
        break
    lst.append(number)
print(sum(lst))