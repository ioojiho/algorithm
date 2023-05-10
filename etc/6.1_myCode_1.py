#1부터 n까지의 합을 계산하는 반복 함수와 재귀 함수
#필수조건: n>=1
#결과: 1부터 n까지의 합을 반환한다.

n = int(input());
sum = 0;

for i in range(1, n+1):
  sum = sum + i;

print(sum);


#문제점: input과 같은 결과값이 나옴. for문안에 print ('test');를 삽입하면 for문만큼 반복되지 않고 한번만 출력됨
#발견한 문제의 원인: VScode로 파이썬을 코딩하는건 처음인데, 
#Run without Dibugging이 아닌, Run Python File in Terminal으로 실행하니 오류가 떴다. 
