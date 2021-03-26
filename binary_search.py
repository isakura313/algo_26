from random import randint

data = list(range(0, 10))


def random_generate(length):
    x = []
    for i in range(1, length):
        x.append(randint(1, length))
    return x


data2 = random_generate(100000)

global i

data = list(range(1, 10))
print(data)
def binary_search(arr, x, high,  counter):
    if high >= arr[0]:
        counter += 1
        mid = (arr[0] + high) // 2 # 5
        # print(mid)
        print(arr[mid])
        if arr[mid] == x:
            return f'индекс числа {mid}, шагов {counter}'
        elif arr[mid] > x:
            return binary_search(arr, x, mid - 1,  counter)
        else:
            return binary_search(arr, x, mid + 1, counter)
    else:
        return -1


print(binary_search(data, 4, len(data),  0))
