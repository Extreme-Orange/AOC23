hold_time = 0
successes = 0
while hold_time <= 46857582:
    if (46857582 - hold_time)*hold_time > 208141212571410:
        successes = successes + 1
        hold_time = hold_time + 1
    else:
        hold_time = hold_time + 1

print(successes)