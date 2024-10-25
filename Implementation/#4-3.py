# 구현 2. 왕실의 나이트

now = input()
y = int(now[1])
x = int(ord(now[0])) - int(ord('a')) + 1  # ord = 문자에 해당하는 유니코드 정수를 반환 (a =97) a=1 ~로 변환

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

count =0

for i in move:
    nexty = y + i[1]
    nextx = x + i[0]
    # 해당 위치로 이동이 가능할때만 카운트 증가
    if nexty >= 1 and nexty <= 8 and nextx >= 1 and nextx <= 8 :
        count += 1

print(count)