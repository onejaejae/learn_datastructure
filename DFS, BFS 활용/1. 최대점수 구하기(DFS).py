import sys
sys.stdin = open("C:\workspaces\자료구조\DFS, BFS 활용\input.txt", "rt")

def DFS(L ,sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        # 문제를 푼 경우
        DFS(L+1, sum+Pscore[L], time + Ptime[L])
        # 문제를 안 푼 경우
        DFS(L+1, sum, time)

if __name__ == "__main__":
    res = -216000
    n, m = map(int, input().split())
    Pscore = []
    Ptime = []

    for _ in range(n):
        x,y = map(int, input().split())
        Pscore.append(x)
        Ptime.append(y)
    
    DFS(0, 0, 0)
    print(res)