import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

# 내 풀이
# def DFS(L):
#     global cnt
#     if L == m:
#         for  r in res:
#             print(r, end=" ")
#         print()
#         cnt +=1
#     else:
#         for i in range(1, n+1):
#             if i in res:
#                 continue
#             res[L] = i
#             DFS(L+1)
#             res[L] = 0

# 해설 풀이
def DFS(L):
    global cnt
    if L == m:
        for  r in res:
            print(r, end=" ")
        print()
        cnt +=1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    ch = [0] * (n + 1)
    DFS(0)
    print(cnt)