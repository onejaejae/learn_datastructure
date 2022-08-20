import sys
sys.stdin = open("C:\workspaces\자료구조\완전탐색기초\input.txt", "rt")

# 내 풀이
# def DFS(L, P):
#     global cnt
#     if L == m:
#         for r in res:
#             print(r, end=" ")
#         print()
#         cnt +=1
#     else:
#         for i in range(1+P,n+1):
#             if check[i] == 0:
#                 check[i] = 1
#                 res[L] = i
#                 DFS(L+1,i)
#                 check[i] = 0

# 해설 풀이
def DFS(L,S):
    global cnt
    if L == m:
        for r in res:
            print(r, end=" ")
        print()
        cnt+=1
    else:
        for i in range(S, n+1):
            res[L] = i
            DFS(L+1, i+1)

if __name__ == "__main__":
    cnt = 0
    n,m = map(int, input().split())
    res = [0] * m
    DFS(0,1)
    print(cnt)