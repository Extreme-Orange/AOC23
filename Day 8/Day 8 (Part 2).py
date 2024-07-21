import math

fhand = open('input.txt')
input = fhand.read()
path = input.split('\n\n')[0] # Sequence of L/R to follow
fhand.seek(0)
map = list()
map1 = dict() # Dictionary that contains node as the key and tuple of L/R as value

for line in fhand:
    map.append(line.rstrip('\n'))

for i in map[2:]:
    map1[i[0:3]] = (i[7:10], i[12:15])

count = 0
position_count = list()
pos = list() # A dictionary to track each position

for node in map1:
    if node[2] == 'A':
        pos.append(node)
    else:
        continue


for s in range(0, 6):
    while pos[s][2] != 'Z':
        for x in path:
            for i in pos:
                if x == 'L':
                    pos[pos.index(i)] = map1[i][0]
                elif x == 'R':
                    pos[pos.index(i)] = map1[i][1]
            print(pos)
            count += 1
    position_count.append(count)

print(position_count)
print(math.lcm(position_count[0], position_count[1], position_count[2], position_count[3], position_count[4], position_count[5])/6)
# I spent so long figuring out why my answer was wrong, only to realise i needed to divide by 6 because all movements count as 1 step, not 6 steps
