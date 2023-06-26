d = [0] * 100 # 메모이제이션을 하기 위한 리스트 초기화

def fibo(x):
    # 종료 조건 (1or2 일때 1을 반환한다)
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환한다
    if d[x] != 0: # 메모가 안된거지 이게
        return d[x] # 그대로 반환한다

    # 아직 계산하지 않은 문제라면? 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))