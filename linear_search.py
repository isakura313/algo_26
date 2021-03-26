from random import randint


data = list(range(1, 1000000))

def random_generate(length):
    x = []
    for i in range(1, length):
        x.append(randint(1, length))
    return x
data2 = random_generate(100000)

def search(arr, x):
    for i in range(len(arr)):
        # print(i)
        if arr[i] == x:
            return i
    return -1


print(search(data, 75545))
# print(search(data2, 75545))
