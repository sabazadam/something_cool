def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(3,4,5,6,7,8))