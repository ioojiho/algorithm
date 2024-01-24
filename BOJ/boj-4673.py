# s[0]부터 s[10000]까지
s = [0] * 10001

for i in range(1, 10000):
  sum = i
  while len(str(i)) > 1:
    sum += (i % 10)
    i //= 10
  if len(str(i)) == 1:
    sum += i
  if sum <= 10000 and s[sum] == 0:
    s[sum] = 1
    
for i in range(1, 10000):
  if s[i] == 0:
    print(i)
