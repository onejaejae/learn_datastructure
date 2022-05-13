# 연습1의 해쉬 테이블 코드에 Chaining 기법으로 충돌해결 코드를 추가
from pkgutil import get_data


hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data, value):
    index_key = get_key(data)

    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0]  == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])    
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_hash(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
            else:
                return None
    else:
        return None     



save_data('Dddd', '12010')
save_data('Dsate', '33333')

print(read_hash('Dddd'))