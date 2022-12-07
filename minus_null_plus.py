n = int(input())
otric = []
null = []
poloj = []
for i in range(n):
    num = int(input())
    if num < 0:
        otric.append(num)
    if num == 0:
        null.append(num)
    if num > 0:
        poloj.append(num)
print(*otric,sep="\n")
print(*null,sep="\n")
print(*poloj,sep="\n")