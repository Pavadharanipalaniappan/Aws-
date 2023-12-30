def checkLastChar(file_name,last):
    count=0
    print("Words Ending with "+last)
    file=open(file_name)
    lines=file.readlines()
    for line in lines:
        words=line.split()
    for word in words:
        if word[-1]==last:
            count+=1
            print("Word : {}".format(word))
    print("Count = ",count)
checkLastChar("article.txt","e")