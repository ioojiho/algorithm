n = int(input())

cow_arr = [''] * 11 #cow_arr[0] ~ cow_arr[10]
move = [0] * 11
for _ in range(n):
  cow, locate = map(int, input().split())
  if cow_arr[cow] == '':
    cow_arr[cow] = locate
  elif cow_arr[cow] != locate:
    cow_arr[cow] = locate
    move[cow] += 1

print(sum(move))
  