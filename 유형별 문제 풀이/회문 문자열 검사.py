#import sys
#sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

# 나의 풀이
n = int(input())
for j in range(n):
    result = input()
    result = result.upper()
    length = len(result)
    count = 1
    
    # 짝수
    if length % 2 == 0:
        left = result[:length//2]
        right = result[length - 1:(length//2)-1: -1]
    # 홀수
    else:
        left = result[:length//2]
        right = result[length - 1: (length//2): -1]
    
    for i in range(length // 2):
        if left[i] != right[i]:
            print("#%d NO" %(j+1))
            break
    else:
        print("#%d YES" %(j+1))


# 해설 풀이
# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)

#     for j in range(size // 2):
#         if s[j] != s[-1 -j]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))
