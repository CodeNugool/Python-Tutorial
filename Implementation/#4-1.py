# 구현 4-1 상하좌우 

n = int(input())  # 문자로 반환시 str 사용
move = input().split()
x, y = 1, 1

# LRUD에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
movetypes =['L', 'R', 'U', 'D']

# 이동
for i in move:
    # 이동 후 좌표 구하기
    for j in range(4):
        if i == movetypes[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    #공간을 벗어나는 경우 무시
    if nx <1 or ny <1 or nx>n or ny>n :
        continue  # continue = 반복을 수행하는 도중에 해당 조건을 만족하는 경우 반복문 나머지 코드를 1회 건너뛰고 계속해서 반복문을 수행함
                  # 즉 수행 후 nx < 1 이라면 아래 이동 수행 부분을 생략하여 이동안한 것이 됨 
    
    # 이동수행
    x, y = nx, ny

print(x, y)
