t = int(input())

result = [0] * t
for i in range(t):
  n, m = map(int, input().split())

  result[i] = 1;
  for _ in range(n):
    result[i] *= m
    m -= 1
  for _ in range(n):
    result[i] /= n
    n -= 1

for i in range(t):
  print(int(result[i]))