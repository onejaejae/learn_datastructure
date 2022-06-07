# 동전 문제
coin_list = [500, 100, 50, 1]

def min_coin_count(value):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_num = value//coin
        total_coin_count = total_coin_count + coin_num
        value %= coin
        details.append([coin,coin_num])
    return total_coin_count, details

print(min_coin_count(4720))