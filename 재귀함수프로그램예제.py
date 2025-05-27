def hanoi_tower(n, start, end) : # n=원판개수 start=시작탑 end=종료
    if n == 1 : # 원판이 한개인 경우에는 한번에 완료
        print(start, end)
        return

    hanoi_tower(n-1, start, 6-start-end)
    # 1단계 : n-1(제일 큰 원판 제외 나머지) 거쳐가는 보조 기둥으로 옮김
    print(start, end)
    # 2단계 : 큰 원판을 주 목표 기둥으로 옮김
    hanoi_tower(n-1, 6-start-end, end)
    # 3단계 : 다시 제일 큰 원판을 제외한 나머지 원판을 목표 기둥으로 옮김

n = int(input())
print(2**n-1)   # 총 이동 회수는 2^n - 1
hanoi_tower(n, 1, 3)
