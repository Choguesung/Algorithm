T = int(input())

for i in range(1, T+1):
    a,b = map(int,input().split())

    target = (a+b) % 24

    print("#"+str(i)+" "+str(target))
