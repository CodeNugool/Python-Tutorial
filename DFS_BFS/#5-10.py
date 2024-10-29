# 5-10 음료수 얼려먹기 


n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
# graph = [list(map(int, input().split())) for _ in range(n)] 도 가능할 듯

# DFS로 특정한 노드 및 연결된 노드 방문
def dfs(x, y): 
  # 주어진 범위를 벗어나는 경우 즉시 종료
  if x <= -1 or x >=n or y <= -1 or y >=m:  # 0~n-1 범위 0~m-1 범위
    return False  # return = 함수의 결과값을 반환하고 함수를 빠져나옴 = 이 경우는 False 반환
                  # 즉, return 만 적는다면 결과값 반환 없이 함수만 빠져나옴
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    graph[x][y] =1 # 해당 노드 방문 처리 => 즉, 방문한 노드는 1로 바꿈으로서 중복안되게 카운트 가능
    # 상, 하, 좌, 우 위치 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True # 밑에 보면 True 일때 개수 카운트함
  return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 dfs 수행
    if dfs(i,j) == True:
      result += 1

print(result)