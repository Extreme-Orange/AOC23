# Adding up
total = 0
for row in map2:
    for i in range(0, len(map2[row])-1, 2):
        total += map2[row][i+1] - map2[row][i] - 1
        print(total)
    print(row)

print(total)
print(map2)




# Checking for odd rows
for row in map2:
    if len(map2[row]) % 2 == 0:
        continue
    else:
        print(row)


total = 0
for row in map2:
    if len(map2[row]) % 2 == 0:
        for i in range(0, len(map2[row])-1, 2):
            total += map2[row][i+1] - map2[row][i] - 1
    else:
        for i in range(0, len(map2[row])-1):
            if map2[row][i+1] - map2[row][i] - 1 == 0:
                continue
            elif map2[row][i+1] - map2[row][i] - 1 > 0:
                if i % 2 != 0:
                    continue
                else:
                    total += map2[row][i+1] - map2[row][i] - 1

print(total)
print(map2)