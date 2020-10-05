n = int(input())
m = int(input())

d = {k: list(map(int, input().split())) for k in range(0, n)}

x = int(input())
y = int(input())

result_list = []

try:
    if x != 0 and x != n:
        result_list.append((d[x-1][y]))
except LookupError:
    pass

try:
    result_list.append((d[x+1][y]))
except LookupError:
    pass

try:
    if y != 0 and y != m:
        result_list.append((d[x][y-1]))
except LookupError:
    pass

try:
    result_list.append((d[x][y+1]))
except LookupError:
    pass


result_list.sort()
print(' '.join(map(str, result_list)))
