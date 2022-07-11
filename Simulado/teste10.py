a, b, c =7, 2, 5

if a < b:
    if b < c:
        a = b
    else:
        b = c
else:
    if b > c:
        b = a
    else:
        a = c
print(a, b, c) # 5 2 5 #