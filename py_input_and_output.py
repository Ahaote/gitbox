import sys

'''
高效输入问题
'''

#第一种，处理单行单参数 比如单个2
# n = sys.stdin.readline().strip()
# print(n)


#第二种，单行多参数 比如 3 5 6
nums = list(map(int, sys.stdin.readline().split()))
print(nums)


#第三种，固定行数的二维数组
n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#第四种，不定行数的终止符检测
for line in sys.stdin:
    a,b = map(int, line.strip().split())
    if a == 0 and b == 0:
        break
    print(a + b)

