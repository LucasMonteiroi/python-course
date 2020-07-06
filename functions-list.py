# Execute functions with lists
supplies = ['pencil', 'book', 'pen', 'paper']
for i in range(len(supplies)) :
    print('In the index ' + str(i) + ' of supplies we have ' + str(supplies[i]))

# Using multiple assignment
dog = ['big', 'black', 'sleeping']
size, color, now = dog # assigning one by one in order from array
print('The dog is ' + color + ' and ' + size + ' and now is ' + now)
print('We have a new dog!')
size, color, now = 'small', 'gray', 'eating' # Pass new values in one line in order
print('The dog is ' + color + ' and ' + size + ' and now is ' + now)

# Incrementing and decrementing values in variables
spam = 2
print(str(spam))
print('New value')
spam += 1
print(str(spam))
print('New value')
spam -=2
print(str(spam))