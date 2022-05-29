def func(num):
    print(num)

    if num <= 1:
        return num

    if num % 2 == 0:
        return func(num // 2)
    else:
        return func((num * 3) +1)

def fun2(data):
    if data == 1:
        return data
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    
    return fun2(data-1) + fun2(data-2) + fun2(data-3)

print(fun2(5))
    

