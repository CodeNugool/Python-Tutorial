# 구현 4-2 시각 

# 본 문제의 팁 = "문자열"로 바꾸어 "포함" 하는지 확인한다.

h = int(input())

count = 0

for i in range(h+1): #h시 59분 59초 까지 확인
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
