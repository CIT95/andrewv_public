def fizz_buzz(num):
    res = num
    if num % 15 == 0:
        res = 'FizzBuzz'
    elif num % 5 == 0:
        res = 'Buzz'
    elif num % 3 == 0:
        res = 'Fizz'
    return res
try:
    number = int(input('Enter a number: '))
    if number < 1:
        for i in range(100):
            print(fizz_buzz(i+1))
    else:
        print(fizz_buzz(number))
except ValueError:
    print('You did not enter a number.')
