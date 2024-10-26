# 5-4 재귀함수 종료 예제


# 스택 구조 이용
# 가장 마지막에 호출한 함수가 수행을 끝내야 그 앞의 함수 호출이 종료됨.

def recursive_function(i):
   # 100번째 출력했을 때 종료되도록 조건 명시
  if i == 100:
    return  # 함수가 호출될 때 불러오는 결과

  print(i, '번째 재귀함수에서', i+1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i+1)
  print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)