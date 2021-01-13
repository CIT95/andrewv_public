while True :
    print('Enter a starting number: (q to quit)')
    start = input()
    if start == 'q':
        break
    start = int(start)
    print('Enter an ending number: ')
    end = int(input())
    if start > end:
        print('Ending number must be larger than starting number')
        continue
    else:
        for i in range(start,end+1):
            print(i)
