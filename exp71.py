def count(filename):
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            if not line.startswith('T') and not line.startswith('t'):
                count += 1
        return count
filename = "story.txt"
count = count(filename)
if type(count) == int:
    print("No.of lines not starting with T ",count)
else:
    print(count)
