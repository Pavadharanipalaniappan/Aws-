def display(file):
    with open(file,'r') as f:
        for line in f:
            words=line.split()
            for word in words:
                if len(word)<4:
                    print(word)
file='story3.txt'
display(file)