def display_words():
    file = open("story.txt","r")
    data = file.read()
    words = data.split()
    for word in words:
        if len(word) < 4:
            print(word, end=" ")
    file.close()

display_words()