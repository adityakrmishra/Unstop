n=int(input())
unique=[]
for i in range(n):
  x=input()
  if x in unique:
    unique.remove(x)
  else:
    unique.append(x)
k=int(input())
if len(unique)<k:
  print(-1)
else:
  print(unique[k-1])
