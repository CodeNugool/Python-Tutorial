# 4. 1이 될 때까지

n, k = map(int, input().split())
count = 0


# tip : 진짜로 1씩 빼지는 않아도 됨. 계산만.
while True:
  target = (n // k) * k
  count += (n-target)
  n = target

  # target이 k 보다 작을 때 반복문 탈출
  if n < k :
    break
  #if가 아니라면 아래 수행
  count += 1
  n //= k
  
count += (n-1)    
print(count)
