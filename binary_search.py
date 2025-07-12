l = 1
r = 2
target = 1

step = 0
while l < r:
    step+=1
    print(step)
    m = l + ( r - l ) // 2 
    if m == target:
        print(m)
        break

    elif m < target:
        l = m + 1

    else:
        r = m 
