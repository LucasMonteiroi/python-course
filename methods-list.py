# Using methods in list
firstList = ['John', 'Jason', 'Elliot', 'Richard']
print('First list' + str(firstList))
print('Elliot has in index: ' + str(firstList.index('Elliot')))

print('Alex not in the list, lets include him?')
firstList.append('Alex') # Insert on last slot
print(str(firstList))

print('Include Michael too')
firstList.insert(0, 'Michael') # Insert on first slot
print(str(firstList))

print('Now we will remove Jason from the list')
firstList.remove('Jason') # We can remove on this too: firstList.remove(firstList[1])
print(str(firstList))

print('We will remove John too')
del firstList[1]
print(str(firstList))

# Sorting the lists
print('Sorting the list')
firstList.sort()
print(str(firstList))

print('Sorting the list reversed')
firstList.sort(reverse = True)
print(str(firstList))