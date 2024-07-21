def check(x):
    n = 0
    for item in x:
        if item != 0:
            n += 1
        else:
            continue
    if n == 0:
        return False
    else:
        return True               


def hist_diff(x):
    history = list()
    history.append(x)
    while check(history[len(history)-1]) == True:
        next_level = list()
        for i in range(0, len(x)-1):
            next_level.append(int(x[i+1])- int(x[i]))
        history.append(next_level)
        x = next_level
    return history


def b_extrap(x):
    n = 0
    for i in range(len(x)-1, -1, -1):
        n = int(x[i][0]) - n
    return n

fhand = open('input.txt')
sum = 0

for line in fhand:
    nums = line.split()
    sum += b_extrap(hist_diff(nums))

print(sum)
    
