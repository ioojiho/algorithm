a = int(input())

#int를 string으로 변환
def make_str(a):
  if a>=0 and a<10:
    a = str(0)+str(a)
  else:
    a = str(a)
  return a

a = make_str(a)
b = a
cnt = 0
while(True):
  sum = int(b[0]) + int(b[1])
  sum_str = make_str(sum)
  b = b[1] + sum_str[1]
  cnt +=1
  if (a == b):
    break

print(cnt)
  
  
  
  
  
  