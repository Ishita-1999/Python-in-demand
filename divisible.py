a = []
value=[i for i in input().split(',')]
for p in value:
    int p = int(p, 2)
    if not int p % 5:
        a.append(p)

print ','.join(a)