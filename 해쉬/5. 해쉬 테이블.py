import hashlib

# string을 encode() 함수를 통해 byte 형태로 변환
# data = 'test'.encode()

# hash_object = hashlib.sha1()
# # byte 형태를 넣어줘야함
# hash_object.update(data)
# hex_dig = hash_object.hexdigest()
# print(hex_dig)

# 연습 2의 Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수를 sha256 해쉬 알고리즘을 사용하도록 변경해보기
hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    # 16진수로 변환
    hex_dig = hash_object.hexdigest()
    # 10진수 int 형으로 변환
    return int(hex_dig, 16)

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

save_data('da', '0101010')
save_data('dh', '12121212')
print(read_hash('dh'))
print(read_hash('da'))
