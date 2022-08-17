cnt = 0
def solution(n, k):
    
    res = [0] * n

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

    DFS(0)

print(solution(3,5))