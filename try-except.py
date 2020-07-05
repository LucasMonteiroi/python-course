def div42by(number) :
    try:
        return 42 / number
    except ZeroDivisionError :
        print('Error: zero division')

print(div42by(0))
print(div42by(2))