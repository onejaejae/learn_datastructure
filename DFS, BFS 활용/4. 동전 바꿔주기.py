# import sys
# sys.stdin = open("C:\workspaces\자료구조\DFS, BFS 활용\input.txt", "rt")

def DFS(L, sum):
    global cnt
    if sum > t:
        return

    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(0, nums[L] + 1):
            DFS(L+1, sum + (coin[L] * i))
            
            

if __name__ == "__main__":
    t = int(input())
    k = int(input())
    coin = []
    nums = []
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        coin.append(x)
        nums.append(y)
    
    DFS(0,0)
    print(cnt)
