# 5-5 팩토리얼 n! 구현


# 1) 반복으로 구현

def factorial_iterative(n):
  result = 1
  # 1부터 n 까지 차례대로 곱하기
  for i in range(1, n+1):
    result *= i
  return result  # retuen = 함수 실행 시 돌려 받는 값




# 재귀적으로 구현한 n!

def factorial_recursive(n):
  if n <= 1:   # n이 1 이하인 경우 1을 반환
    return 1
  # n! = n * (n-1)!를 그대로 코드로 작성
  return n * factorial_recursive(n-1)


# 각각 출력 n=5 일 때.
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))