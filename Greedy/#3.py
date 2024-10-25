# 3. 숫자카드게임

n, m = map(int, input().split())

#행렬 입력받기 리스트.append() = ()값을 리스트 맨 끝에 객체로 추가
card = []
for i in range(n):
  card.append(list(map(int, input().split())))
  # 즉 card[[리스트1], [리스트2], ...] 이렇게 추가

card2=[]
for i in range(n):
  card2.append(min(card[i-1]))

print(max(card2))