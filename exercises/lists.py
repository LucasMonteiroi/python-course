# Lists usage
print(' ------------ Lists ------------- ')
print()

listString = ['cow', 'chicken', 'snake', 'dog', 'cat']
print('Printing all list string: ' + str(listString))
print('Printing an last item from list string: ' + str(listString[-1]))
print('The ' + str(listString[-1]) + ' has afraid from')
print('Ordering list from 2 item: ' + str(listString[1:]))
print('Multipling the lists string: ' + str(listString * 3))
print('Removing an element from list: ')
del listString[1]
print(str(listString))
print()
print(' ------------ Double List ------------- ')
print()
doubleList = [['cat', 'dog', 'snake'], [10, 20, 30]]
print('First part of double list: ' + str(doubleList[0]))
print('Element from first part of double list: ' + str(doubleList[0][1]))
print('Second part of double list: ' + str(doubleList[1]))
print('Element from second part of double list: ' + str(doubleList[1][1]))
print()
print(' ------------  ------------- ')
print()
print('Making a string to a list: Hello')
newList = list('Hello')
print(newList)
print()
print(' ------------ Check in Lists ------------- ')
print()
print('Has cow in list string?')
checker = 'cow' in listString
print(str(checker))
print('Has chicken not in list string?')
checker = 'chicken' not in listString
print(str(checker))