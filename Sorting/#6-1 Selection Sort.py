 # 6-1 선택정렬
# 선택정렬 = 매번 가장 작은 것을 선택하여 맨 앞으로 보냄

# 오름차순

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)): # array의 길이만큼 반복
  min_index = i # 가장작은 원소의 인덱스
  for j range(i+1, len(array)): # i+1부터 array길이까지 반복
    if array[min_index]> array[j]:
      min_index = j 
  array[i], array[min_index] = array[min_index], array[i] # 스와프 : 현재 위치 i에 있는 값과 최소값의 위치에 있는 값을 서로 바꾼다. 이를 통해 현재 위치에는 해당 범위에서 가장 작은 값이 오게 된다.

print(array)