fhand = open('input.txt')
input = fhand.read()
path = input.split('\n\n')[0]
fhand.seek(0)
map = list()
map1 = dict()

for line in fhand:
    map.append(line.rstrip('\n'))

for i in map[2:]:
    map1[i[0:3]] = (i[7:10], i[12:15])

count = 0
pos = 'AAA'

while pos != 'ZZZ':
    for x in path:
        if x == 'L':
            pos = map1[pos][0]
            count += 1
        elif x == 'R':
            pos = map1[pos][1]
            count += 1

print(count)