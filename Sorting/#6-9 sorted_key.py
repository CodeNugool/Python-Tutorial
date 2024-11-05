# 6-9 key 매개변수 활용

# sorted()나 .sort()에서 입력받을 수 있음.
# key 값으로는 하나의 함수가 들어가야 하며, 정렬 기준이 된다.

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
  return data[1]

result = sorted(array, key = setting)
print(result)
