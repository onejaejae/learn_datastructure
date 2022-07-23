from array import array


def solution(L):
    answer = ""
    array = []

    L.sort(key=lambda x: (x[1], x[0]))
    array.append(L.pop(0))
    
    while L:
        for i in range(1,len(L)):
            cnt = 0
            min = 21600000
            print(array)
            for y in array:
                if L[i][0] >= y[0]:
                    cnt += 1

            if cnt == L[i][1]:
                if min > L[i][0]:
                    index = i
                    min = L[i]
                array.append(L.pop(index))
        
        

    return answer

print(solution([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))