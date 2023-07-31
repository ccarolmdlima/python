l = [3,2,1,7,8,9,7]
l1 = [1,34,5,2]
print("primeira iteração do for in")
w = l[0]
y = l[0]
i = t = 0
for x in l:
    print(x)
    if l[i] > w:
        w = l[i]
    if l[i] < y:
        y = l[i]
    i = i + 1
    t = t + x
    print("o maior é ", w)
    print(max(l))
    print("o menor é ", y)
    print(min(l))
