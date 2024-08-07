n = int(input())
money = list(map(int, input().split()))
bg = int(input())

left = 0
right = max(money)

while left <= right:
    mid = (left + right) // 2
    sum = 0

    for i in money:
        # 상한액을 초과하는 경우
        if i > mid:
            sum += mid
        # 상한액보다 낮은 경우
        else:
            sum += i

    if sum <= bg:
        left = mid + 1
    else:  # 예산초과하는경우 상한액을 낮춰야 한다
        right = mid - 1

print(right)
