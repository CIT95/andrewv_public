import pprint
cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}

allCats = []
allCats.append(cat)
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fat-tail', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'orange'})

print(allCats)

theBoard = {'top-L': ' ', "top-M": ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }

pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'
pprint.pprint(theBoard)
theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['low-R'] = 'X'
theBoard['mid-L'] = 'X'
pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] +'|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] +'|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] +'|' + board['low-R'])

printBoard(theBoard)
print(type(42))
print(type('hello'))
print(type(theBoard))
