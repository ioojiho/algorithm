a, b, c = map(int, input().split())
x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
z1, z2 = map(int, input().split())

time = [0] * 100
for i in range(x1, x2):
  time[i] += 1
for i in range(y1, y2):
  time[i] += 1
for i in range(z1, z2):
  time[i] += 1
pay = 0
for i in range(100):
  if time[i] == 1:
    pay += a*1
  if time[i] == 2:
    pay += b*2
  if time[i] == 3:
    pay += c*3 

print(pay)