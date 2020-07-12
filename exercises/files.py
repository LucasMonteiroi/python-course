# Open in read mode
helloFile = open('/Users/lucasmonteiroi/Documents/hello.txt')
fileContent = helloFile.read()
print(fileContent)
helloFile.close()

# Read lines in file
sameFile = open('/Users/lucasmonteiroi/Documents/hello.txt')
print(sameFile.readlines())
sameFile.close()

# Open in write mode
# a means append in file
# w write file will replace entire file
# if you want to create other file, just change folder and/or name
newFile = open('/Users/lucasmonteiroi/git-repo/python-course/output-files/firstFile.txt', 'w')
newFile.write('This is the first file, with interact with user.\n')
print('What is your name?')
newFile.write('Machine: What is your name?\n')
name = input()
newFile.write('User: %s\n' % (name))
newFile.close()

changeFile = open('/Users/lucasmonteiroi/git-repo/python-course/output-files/firstFile.txt', 'a')
changeFile.write('Machine: What is your age?\n')
print('What is your age?')
age = input()
changeFile.write('User: %s\n' % (age))
changeFile.close()
print('Thank you for the answer.')