# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    l = []
    for i in range(a,b + 1):
        l.append(i)
    for i in range(c,d + 1):
        l.append(i)
        
    print(len(set(l)))
