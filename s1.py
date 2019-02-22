# v = dict.fromkeys(['k1', 'k2'], [])
# v['k1'].append(666)
# print(v)
# v["k1"] = 777
# print(v)

# M = [1, 2, 3, 4, 5]
# N = []
# for i in range(5):
#     bai = M[i]
#     for j in range(5):
#         if j != i:
#             shi = M[j]
#             for k in range(5):
#                 if k != i and k != j:
#                     ge = M[k]
#                     num = bai * 100 + shi * 10 +ge
#                     N.append(num)
#
# print(len(N))


# m = [1,2,3,1,2,4]
# print(list(set(m)))


# a = "1,2,3"
# b = a.split(",")
# m = map(lambda x: int(x), b)
# print(list(m))


# print([i*i for i in range(1, 11)])


# import itertools
#
# print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))


# b = [7, -8, 5, 4, 0, -2, -5]
#
# print(sorted(b, key=lambda x: x if x>0 else -x))


# lis = [12,5,8,74,53,15,4]
#
# for i in range(len(lis)-1):
#     if lis[i] > lis[i+1]:
#         tmp = lis[i]
#         lis[i] = lis[i+1]
#         lis[i+1] = tmp
# i = 0
# while i < len(lis) - 1:
#     if lis[i] > lis[i + 1]:
#         lis[i], lis[i + 1] = lis[i + 1], lis[i]
#     i += 1
# print(lis)

# lis = [12, 5, 8, 74, 53, 6, 15, 24]
#
#
# print(lis)

# import math
#
# print(math.floor(5.5))

# {1: 0, 2: 0, 3: 0}
# {'1': 0, '2': 0, '3': 0}
# {(1, 2): 0, (4, 3): 0}
# {[1, 2]: 0, [4, 3]: 0}
# {{1, 2}: 0, {4, 3}: 0}

# kvps = {"1": "$121", "2": 2}
# thecopy = kvps.copy()
# kvps["1"] = 5
# # sum = kvps["1"] + thecopy["1"]
# print(thecopy["1"])

# arr = [1,2,3]
# def bar():
#     global arr
#     arr += [5]
# bar()
# print(arr)
# import time
# st = time.time()
#
def func(m):
    s = str(m)
    return set(s)


for a1 in range(10, 100):
    for b1 in range(10, 100):
        for e1 in range(10, 100):
            c1 = a1 - b1
            p = e1 + c1
            s = func(a1) | func(b1) | func(c1) | func(e1) | func(p)
            if len(s) == 9 and len(func(p)) == 1 and c1 > 10 and p > 100:
                print(a1, b1, c1, e1, p)


# el = 'AB-CD=EF EF+GH=PPP'
# ns = '123456789'
# el = el.replace('=','==').replace(' ', ' and ')
# vs = list(set([s for s in el if s >= 'A' and s <= 'Z']))
# ns = [s for s in ns]
#
#
# def fs(el, vs, ns):
#     if not vs:
#         if eval(el):
#             print(el.replace('and ', '').replace('==', '='))
#     else:
#         v = vs[0]
#         ix = len(ns)
#         while ix:
#             ix -= 1
#             nel = el.replace(v, ns[ix])
#             fs(nel, vs[1:], ns[0:ix]+ns[ix+1:])


# print('time:%dms'%((time.time()-st)*1000))

# 6811ms

# su = 0
# arr = [3, 4, 1, 2, 5, 6, 6, 5, 4, 3, 3, 8]
# for i in arr:
#     if arr.count(i) == 1:
#         su += i
# print(su)

