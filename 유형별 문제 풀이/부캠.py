def solution(word):
    keyboard = ["가", "나", "다", "라", "마"], ["아", "자", "차", "카", "타"], ["파", "하", "가", "나", "다"], ["가", "나", "다", "라", "마"], ["가", "나", "다", "라", "마"]
    min = 999999
    flag = True
    total = 0
    count = 0
    array = list()

    for i in range(5):
        for j in range(5):
            keyboard[i][j] = j,i, keyboard[i][j]


    for data in word:
        for i in range(5):
            for j in range(5):
                if data in keyboard[j][i][2]:
                    array.append(keyboard[j][i])
                    flag = False
                    break
            if flag == False:
                print("a")
                flag = True
                break
        else:
            total += 20
            count += 1        
        
    print(total)

   #print(keyboard[0][0][2])


solution("가나쿠")