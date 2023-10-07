m = int(input())
n = int(input())

result = []

for i in range(m, n+1): #i = m부터 n까지
  if i==2:
      result.append(2)
  for j in range(2, i): #j = 2부터 i-1(자기자신제외)까지
    if i%j == 0:
      break;
    if j == i-1:
      result.append(i)

if len(result)==0:
  print(-1)
else:
  print(sum(result))
  print(result[0])