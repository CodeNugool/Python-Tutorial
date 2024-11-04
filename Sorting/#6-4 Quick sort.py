# 6-4 퀵 정렬
# 퀵 정렬 = 기준데이터(피벗)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.

# 호어 분할(Hoare Partition) 기준 , 재귀함수 사용시 단순, 시간은 비효율적


# 1. 리스트에서 첫 번째 데이터를 피벗으로 정한다.

# 2. 왼쪽부터 피벗보다 큰 데이터 선택
# 3. 오른쪽부터 피벗보다 작은 데이터 선택
# 4. 두 데이터의 위치를 스와프
# 5. 왼쪽, 오른쪽 데이터가 엇갈린 경우 "작은 데이터"와 피벗을 스와프
# 6. 분할 혹은 파티션 = 피벗을 기준으로 왼쪽 = 작은 데이터, 오른쪽 = 큰 데이터

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:      # 원소가 1개인 경우 종료
    return

  pivot = start     # 피벗 = 첫번째 원소
  left = start + 1
  right = end
  while left <= right:  # 왼쪽 오른쪽 데이터 위치가 엇갈릴 때까지 반복
    while left <= end and array[left] <= array[pivot]:  # 왼쪽 데이터가 피벗보다 작거나 같을 때까지 반복
      left += 1
    while right > start and array[right] >= array[pivot]:  # 오른쪽 데이터가 피벗보다 크거나 같을 때까지 반복
      right -= 1
    if left > right : # 엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 작은데이터와 큰 데이터 교체
      array[left], array[right] = array[right], array[left]

  # 분할 이후 왼쪽, 오른쪽 각각 정렬 수행
  quick_sort(array, start, right -1)   # 재귀함수
  quick_sort(array, right +1, end)

quick_sort(array, 0, len(array)-1)
print(array)
    