# Linear Probing 기법

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] =[index_key, value]

def read_hash(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            # 빈 슬롯은 해당 데이터가 저장되지 않았다는 뜻
            # 충돌이 일어나면 다음 슬롯에 저장하는 flow이므로
            if hash_table[index] == 0:
                return  None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
            else:
                return None
    else:
        return None

print(hash_function(get_key("d")))

print(hash_function(get_key("dsa")))
