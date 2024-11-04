#6-5 퀵정렬 (파이썬 버전)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1: 
    return array

  pivot = array[0]   # 피벗 = 첫번째 원소
  tail = array[1:]   # 피벗을 제외한 리스트 = tail

  left_side = [x for x in tail if x <= pivot]  # tail에서 피벗보다 작은 값들을 left_side 리스트에 저장
  right_side = [x for x in tail if x > pivot]  # tail에서 피벗보다 큰 값들을 right_side 리스트에 저장

   # [x for x in tail .. ]:
   # tail 리스트에 있는 원소를 하나씩 x에 대입합니다.
   # 조건이 통과된 값들로 새로운 리스트를 만듭니다.

   # if x <= pivot:
   # tail 리스트의 각 원소 x가 기준값 pivot보다 작거나 같은지를 검사합니다.
   # 조건을 만족하는 원소만 left_side 리스트에 포함됩니다.
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)  # 재귀호출을 이용해 전체 정렬

print(quick_sort(array))