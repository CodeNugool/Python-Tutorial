# 6-3 삽입정렬 Insertion Sort
# 삽입정렬 = 데이터를 하나씩 확인하며 적절한 위치에 삽입
# 특징 = 그 앞까지의 확인한 데이터들은 이미 (오름차순)정렬되어 있음
#     = 삽입 위치 선정방법 (삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추면 된다.)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 삽입정렬은 0이 아닌 1부터 시작
  for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 for문
    if array[j] < array[j - 1]: # 비교 후 왼쪽이 크면
      array[j], array[j-1] = array[j-1], array[j]  # 왼쪽으로 한칸 씩 이동
    else: # 자기보다 작은 데이터를 만나면 멈춤
      break

print(array)
