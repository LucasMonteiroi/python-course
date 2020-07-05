def hello(name) :
    print('Hello ' + name)
    print('Good to see you')

def lenName(name) :
    print('Your name has ' + str(len(name)) + 'letters in it')

print('What is your name?')
name = input()
hello(name)
lenName(name)