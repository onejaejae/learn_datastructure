def solution(n, arr1, arr2):
    res = []
    res2 = []
    answer = []

    for i in range(n):
        binaryNum = list(format(arr1[i], 'b'))
        binaryNum2 = list(format(arr2[i], 'b'))

        if len(binaryNum) < n:
            while len(binaryNum) < n:
                binaryNum.insert(0,'0')
        if len(binaryNum2) < n:
            while len(binaryNum2) < n:
                binaryNum2.insert(0,'0')
    
        res.append(binaryNum)
        res2.append(binaryNum2)

    for i in range(len(res)):
        str =""
        for j in range(len(res)):
            if res[i][j] == "1" or res2[i][j] == "1":
                str += "#"
            elif res[i][j] == "0" and res2[i][j] == "0":
                str+= " "
        answer.append(str)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))