import math
sqrt = math.sqrt
import sys
while True :                    # main loop to rerun program
    while True:                 # loop for inputing starting number
        start = input('Enter a starting number: (q to quit): ')
        if start == 'q':
           sys.exit() 
        try:
            start = int(start)  # tries to cast to int
            assert start >= 0   # makes sure no negatives
            break               # no errors, so continue with program
        except ValueError:      # a non number was entered
            print('You did not enter a number. Try again')
        except AssertionError:  # a negative number was entered
            print("You entered a negative number. Try again")
    while True:                 # loop for inputing ending number
        end = input('Enter an ending number: ')
        try:
            end = int(end)      # tries to cast to int
            assert end > start  # makes sure the ending number is greater than the starting number
            break               # no errors, so continue with program
        except ValueError:      # a non number was entered
            print('You did not enter a number. Try again')
        except AssertionError:  # ending number was not greater that starting number
            print('Ending number must be larger than starting number. Try again')

    for i in range(start,end+1): # prints all prime numbers between start and end
        prime = True
        if i > 1:
            for j in range(2, 1 + int(sqrt(i))):
                if (i % j) == 0:
                    prime = False
                    break
            if prime:
                print(i)
