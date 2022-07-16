from ast import Return


def solution(N):
    array = []

    if N % 2 == 0:
        for i in range(1,(N//2)+1):
            array.append(i)
            array.append(-1*i)
    else:
        for i in range(1,(N//2)+1):
            array.append(i)
            array.append(-1*i)
        array.append(0)

    print(array)
    print(sum(array))
    return array
    
solution(99)
