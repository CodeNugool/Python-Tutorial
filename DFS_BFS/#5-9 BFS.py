# BFS 5-9 


# BFS(Breadth First Search) = 너비 우선 탐색 = 가까운 노드부터 탐색
# 큐 자료 이용 (선입선출), O(N) 시간 소요, 일반적으로 DFS보다 빠름

from collections import deque  # deque 라이브러리 사용


# BFS 메서드 정의
def bfs(graph, start, visited):
  
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  
  # 큐가 빌 때까지 반복
  while queue:  # 큐가 비어있지 않다면 반복
    
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')

    #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:  # visited[i] = False인 경우 = 방문하지 않았다면,
        queue.append(i)   # 큐에 추가
        visited[i] = True  # 방문처리



# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [], # 보통 1부터 시작하므로 0번은 비워줌
  [2, 3, 8], # 1번 노드와는 2, 3, 8 연결되어 있음
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 1차원 리스트로 표현
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)