# 6-2 스와프 
# 스와프 = 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업

# 0 인덱스와 1 인덱스의 원소 교체하기

array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)