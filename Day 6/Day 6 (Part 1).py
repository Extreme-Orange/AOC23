time = (46, 85, 75, 82)
best_dist = (208, 1412, 1257, 1410)
results = list()
n = 0

for i in time:
    hold_time = 0
    successes = 0
    while hold_time <= i:
        if (i - hold_time)*hold_time > best_dist[n]:
            successes = successes + 1
            hold_time = hold_time + 1
        else:
            hold_time = hold_time + 1
    results.append(successes)
    print(successes)
    n = n+1

total = 1
for i in results:
    total = total * i

print(total)

    
    

