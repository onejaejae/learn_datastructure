import random

def selection_sort(data):
    for stand in range(len(data) -1):
        lowest = stand
        
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        
        data[stand], data[lowest] = data[lowest], data[stand] 
    return data

# 0~100 중 길이가 10인 random list 생성
data_list = random.sample(range(100), 10)
print(selection_sort(data_list))