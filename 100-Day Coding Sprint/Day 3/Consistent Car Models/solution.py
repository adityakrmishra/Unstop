s = input()
n = int(input())
arr = list(map(str, input().split()))
allowed_components = set(s)
count = 0

for model in arr:
    if all(component in allowed_components for component in model):
        count += 1

print(count)
