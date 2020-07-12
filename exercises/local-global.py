def spam() :
    global eggs
    eggs = 'Hello'
    print(eggs)

def bacon(eggs) :
    print('The bacon will cook with ' + str(eggs))

eggs = 2
bacon(eggs)
spam()
