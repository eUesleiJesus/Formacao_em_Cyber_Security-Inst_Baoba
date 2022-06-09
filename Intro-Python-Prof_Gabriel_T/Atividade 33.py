c = 0

for x in range(25, 51):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x)

