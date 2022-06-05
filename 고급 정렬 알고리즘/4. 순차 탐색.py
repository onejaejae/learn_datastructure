from random import *

rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1,100))

print(rand_data_list)

def sequencial(data_list, search_data):
    for i in range(len(data_list)):
        if search_data == data_list[i]:
            return True
    
    return False

print(sequencial(rand_data_list, 10))
