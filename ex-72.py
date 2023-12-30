def count_words():
    file = open("notes.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word =="the":
            count += 1
    print("The occurrence of the word 'the' is:",count)
    file.close()

count_words()