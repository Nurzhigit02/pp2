def Numbers(a):
    for i in range(a, -1, -1):
        yield i


n = int(input())

nums = Numbers(n)

for i in nums:
    print(i, end = " ")