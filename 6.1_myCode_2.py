
sum = int(input());

def recursiveSum (n):
  if (n==1): 
    return 1;  
  return n + recursiveSum(n-1)

print(recursiveSum(sum));

#재귀함수를 사용할 때는 반드시 종료조건 설정하기!