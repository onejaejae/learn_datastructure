def DFS(L):
    global cnt
    if L == 3:
        cnt += 1
        if cnt == k:
            arr = []
            for r in res:
                arr.append(r)
            print(arr)
            exit(1)
    else:
        for i in range(1,n+1):
            if i in res:
                continue
            res[L] = i
            DFS(L+1)
            res[L] = 0


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    res = [0] * n
    cnt = 0
    DFS(0)
