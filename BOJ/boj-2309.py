num = []
for i in range(9):
  n = int(input())
  num.append(n)

left = sum(num) - 100
num.sort()

for i in num:
  if len(num) == 9:
    for j in num[num.index(i)+1:]:
      summ = i+j
      if summ == left:
        num.remove(i)
        num.remove(j)
        break
      
for i in num:
  print(i)
