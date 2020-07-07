print('Hello there\nHow are you?')
print("This is Lucas's dog")
print('This is Lucas\'s cat')
print(r'This is Lucas\'s fish') # raw string
print("""Lucas work with development 
since 2014, beginning with C#""")
spam = 'Hello'
print(spam)
print(spam[0])
print(spam[1:5]) # substring
print(str('Hello' in spam))
print(str('x' in spam))

print(spam.upper())
print(spam.lower())
print('Say something:')
word = input()

print(word.upper())
print(word.lower())
print('Lower ' + str(word.islower()))
print('Upper ' + str(word.isupper()))
print('Alpha ' + str(word.isalpha()))
print('AlNum ' + str(word.isalnum()))
print('Decimal ' + str(word.isdecimal()))
print('Space ' + str(word.isspace()))
print('Title ' + str(word.istitle()))
print('StartsWith ' + str(word.startswith('Oi')))
print('EndsWith ' + str(word.endswith('Tchau')))
print('Join ' + str(' '.join(word)))
print('Split ' + str(word.split('\n')))
print('rjust ' + str(word.rjust(10)))
print('ljust ' + str(word.ljust(10)) + 'end')
print('center ' + str(word.center(10, '-')))
print('Strip ' + word.strip())
print('Lstrip ' + word.lstrip())
print('Rstrip ' + word.rstrip())