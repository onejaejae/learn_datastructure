def solution(A, B):
    A.sort()
    B.sort()
    print(A, B)
    i = 0
    for a in A:
        # print(B[i], a)]
        while i < len(B) - 1 and B[i] < a:
            print(i)
            i += 1
        if a == B[i]:
            print(a)
            return a
    return -1


print(solution([3,9], [1,9,2,5,3]))