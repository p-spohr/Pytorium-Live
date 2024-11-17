print('Hi!')

def add(*args):
    temp = 0
    for num in args:
        erst_str = f'{temp} + {num}'
        temp += num
        print(f'{erst_str} = {temp}')

add(1,2,3)
