# a = "fsijofosj"
# print(a[-2:])

# a = range(9,-1,-3)
# print(list(a))

# lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 32769, 65536, 4294967296]
# di = dict()
# for i in lst:
#     if len(str(i)) in di.keys():
#         di[len(str(i))].append(i)
#     else:
#         di[len(str(i))] = [i]
# print(di)
# from functools import reduce
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# cst = []
# cst.extend(lst)
# print(cst)

# print(reduce(lambda x, y: x+y, lst))
# print(lst[0] + lst[1] + lst[2])

# lst = [7, -8, 5, 4, 0, -2, -5]

# lis = ['a', 'b', 'c', 'd', 'e']
# print(lis[10:])

# print(2**4)

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%s * %s = %s' % (i, j, i * j))


# a = "some_string"
# print(id(a))
# b = "some" + "_" + "string"
# print(id(b))

# a = "wtf"
# b = "".join(['w', 't', 'f'])
# print(id(a), id(b))
# 2389937252312 2389938017480

# some_dict = dict()
# some_dict[5.5] = "Ruby"
# some_dict[5.0] = "JavaScript"
# some_dict[5] = "Python"
#
# print(some_dict[5])

# def some_func():
#     try:
#         return 'from_try'
#     finally:
#         return 'from_finally'
#
#
# print(some_func())

# some_string = "wtf"
# some_dict = {}
# for i, some_dict[i] in enumerate(some_string):
#     pass
# print(some_dict)

# for i in range(4):
#     print(i)
#     i = 10

# array = [1, 8, 15]
# g = (x for x in array if array.count(x) > 0)
# array = [2, 8, 22]
# print(list(g))

# array_1 = [1, 2, 3, 4]
# g1 = (x for x in array_1)
# array_1 = [1, 2, 3, 4, 5]
# print(list(g1))
#
# array_2 = [1, 2, 3, 4]
# g2 = (x for x in array_2)
# array_2[:] = [1, 2, 3, 4, 5]
# print(list(g2))

# a = 1024; b = 1024
# print(a is b)

print([] is [])
