# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
if n==1 and m==0:
    print(1)
else:
    d1,d2,visited={},{},{}
    for i in range(m):
        a,b=map(int,input().split())
        if (a,b) not in visited:
            if b not in d1:
                d1[b]=1
            else:
                d1[b]+=1
            visited[(a,b)]=True
        if a not in d2:
            d2[a]=True

    for i in d1:
        if d1[i]==n-1 and i not in d2:
            print(i)
            break
    else:
        print(-1)
