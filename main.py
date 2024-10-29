# 5-11 미로탈출 


# BFS deque 사용 시 빼먹지 말기
from collections import deque


n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력
graph = []
for i in range(n):
  graph.append(list(map(int, input)))


