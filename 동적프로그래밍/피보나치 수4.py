n = int(input())

s = [0, 1, 1]

for i in range(3, n + 1):
    # 하나 이전 + 두개 계속 추가
    s.append(s[i - 1] + s[i - 2])

print(s[n])
