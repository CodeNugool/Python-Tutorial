# 5-11 미로탈출 


# BFS deque 사용 시 빼먹지 말기
from collections import deque


n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 이동할 4가지 방향 정의(상, 하, 좌, 우)
# 예를 들어, dx[0]는 위쪽으로 한 칸 이동, dx[1]은 아래쪽으로 한 칸 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
# BFS 알고리즘을 구현하기 위한 함수를 정의. 시작 위치 (x, y)를 매개변수로 받는다.
def bfs(x, y):
  # 큐 구현을 위해 deque 라이브러리 사용
  # BFS에서 사용할 큐를 초기화하고, 시작 위치 (x, y)를 큐에 추가
  queue = deque()
  queue.append((x, y))
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft() # 큐의 왼쪽 데이터를 삭제하고 "반환" = 현재위치를 꺼냄
    # 현재 위치에서 네방향으로의 위치 확인(상하좌우 반복)
    for i in range(4): 
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음방문하는 경우에만 최단거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1 # 새로운 위치의 값을 현재 위치의 값 + 1로 업데이트하여 최단 거리를 기록
        queue.append((nx,ny)) # 새로운 위치를 큐에 추가
  # 가장 오른쪽 아래까지의 최단거리 반환
  return graph[n-1][m-1] # BFS가 완료된 후, 미로의 오른쪽 아래 구석까지의 최단 거리를 반환

# BFS 수행한 후, 결과 출력
print(bfs(0, 0))