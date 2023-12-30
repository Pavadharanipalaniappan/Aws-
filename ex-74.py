def count_words():
    file = open("article.txt","r")
    count = 0
    count1 = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word == 'this':
            count+=1
        elif word =='these':
            count1+=1
            
    print("this count =",count)
    print("these count =",count1)
    file.close()

count_words()