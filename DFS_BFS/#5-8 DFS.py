# DFS 깊이 우선 탐색 5-8 DFS 예제

# DFS(depth-first search) = 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 그래프 탐색 = 하나의 노드를 시작으로 다수의 노드를 방문


# DFS는 스택 자료구조에 기초하며, 데이터의 개수가 N개인 경우 O(N)의 시간 소요
# DFS는 재귀함수를 이용 시 매우 간결하게 구현할 수 있다.


# DFS 메서드 정의 DFS 깊이 우선 탐색 5-8 DFS 예제

# DFS = 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 그래프 탐색 = 하나의 노드를 시작으로 다수의 노드를 방문


# DFS는 스택 자료구조에 기초하며, 데이터의 개수가 N개인 경우 O(N)의 시간 소요
# DFS는 재귀함수를 이용 시 매우 간결하게 구현할 수 있다.


# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 서치
  visited[v] = True
  print(v, end=' ')
# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]: # visited[i] = False 인 경우
      dfs(graph, i, visited)  # i 방문
      


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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False]*9   # 0~8 까지의 9개 노드 모드 미방문 = False 로 표시, visited = [False, False, False, False, False, False, False, False, False]

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)


