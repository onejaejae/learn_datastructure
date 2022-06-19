test_case = int(input())

for _ in range(test_case):
    n,m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        # 중요도가 가장 높은 문서가 가장 앞쪽에 위치해있다면
        # https://velog.io/@kjy5947/python-max%ED%95%A8%EC%88%98%EC%9D%98-key%EB%B3%80%EC%88%98-%EC%82%AC%EC%9A%A9
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count +=1
            if queue[0][0] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
            