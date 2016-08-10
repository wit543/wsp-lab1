
doc = open('all rounte')
a = []
for line in doc:
    split_line = line.split(">",1)
    a.append(split_line[1].split(" ",1)[0])
print(a)
