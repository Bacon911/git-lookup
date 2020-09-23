def myfunction(text):
    print(text)
    count = 0
    for i in text:
        if i == 'e':
            count += 1
    print('letters "e" occurs', count, 'times')


myfunction('Happiness is not a destination. It is a method of life.')