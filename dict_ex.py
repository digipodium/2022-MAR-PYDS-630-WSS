data = {}
while True:
    word = input("enter a word: ")
    if word:
        if word in data:
            print(word,"=>",data[word])
        else:
            print("not found")
            if input(f'do you know the meaning of {word} (y/n):') == 'y':
                data[word] = input("enter the meaning: ")
    else:
        print('exiting')
        break