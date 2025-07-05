

'''
1.不带下划线代表的变量或者方法，代表公开的，可以直接通过类对象或实例访问与修改
2.单下划线表示该成员为protected,只是不建议外部直接访问
3.双下划线表示开头，比如外部访问obj.__variable不行，但是python解释器会将变量名改写成_ClassName__variable这种形式，
外部可以通过obj._ClassName__variable进行访问,但不推荐。建议封装成员间接访问
为了父子类的私有变量命名不冲突，子类中私有成员名称会被改写为 _SubClass__variable与父类私有成员 _ParentClass__variable 不冲突


'''

# class Test:
#     def __init__(self,a):
#         self.__a = a
# obj = Test(1)
# print(obj._Test__a)

class MovieIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1
    
    def __next__(self):
        try:
            self.__index += 1
            return self.__data[self.__index]
        except IndexError:
            raise StopIteration

class MoiveController:
    def __init__(self):
        self.list_movie = []
    def __iter__(self):
        return MovieIterator(self.list_movie)
    
controller = MoiveController()
controller.list_movie.append("西游记")
controller.list_movie.append("八角笼中")
controller.list_movie.append("封神")

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

print('=' * 30)

'''
Python中自带的迭代器和自定义迭代器
 __iter__() 方法，返回迭代器对象自身(即self)
 __next__() 方法，返回下一个元素或抛出 StopIteration 异常
 
 迭代器只支持前进，不支持回退或重置

'''
#自带的迭代器
list01= [10,20,30]
a = iter(list01)
b = list01.__iter__()

print(next(a))
print(next(b))

print('=' * 30)

'''
Python生成器
一种特殊迭代器,通过按需生成值的特性显著提升内存效率和代码灵活性
1.通过yield,当函数中使用yield而非return时,该函数变为生成器函数。
执行到yield时会暂停,保存当前状态(如局部变量、执行位置),并向调用方返回一个值；下次调用时从暂停处继续执行

2.生成器逐个生成值而非一次性计算所有结果，适用于大数据或无限序列场景，避免内存溢出

3.生成器自动实现__iter__()和__next__()方法,支持通过for循环或next()逐项取值。取值结束时抛出StopIteration异常 (也就是只能遍历一次)
'''

#创建生成器

#1.通过yield
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(countdown(3)) #打印生成器的地址
it = iter(countdown(3))
print(it) #生成器是特殊迭代器，也就是通过迭代器的方式访问
print(next(it)) # 3
print(next(it)) # 2

for i in countdown(5):
    print(i)

print('=' * 30)

#2.通过生成器表达式
squars = (x**3 for x in range(10))
print(squars) #打印生成器地址
print(next(squars))

for i in squars:
    print(i)
# print(next(squars)) 此时再向后打印就会报错

'''
生成器表达式和列表表达式？

生成器表达式的优点就是 省内存， 缺点就是 只能遍历一次了，并且不能下标访问
列表表达式则是能遍历多次以及下标访问，但是就是不省内存
'''

print('=' * 30)

'''
lambda表达式
lambda 参数列表 : 表达式
无需定义函数名，用完即销，但只能包含单个表达式，不能使用 return 或多行代码（比如循环）
'''

#简单lambda表达式
add = lambda a,b : a+b
print(add(3,5))


'''
内置应用函数map

map(function, iterable,...)
参数1:为一个函数,参数2:为一个或多个可迭代对象。表示每个对象都通过函数进行加工。
最后返回一个迭代器对象

map值得注意的是：map是惰性计算的，也就是需要的时候再计算，因此适合处理大规模数据
'''

#map的使用
numbers = [1, 2, 3]
t = (3,2,1)
doubled = list(map(lambda x,y: x * y, numbers, t))
print(doubled)


'''
内置应用函数filter
用于根据指定的函数对可迭代对象（如列表、元组、集合等）中的元素进行筛选，
返回一个包含所有满足条件的元素的迭代器,也是惰性的，需要才计算适合处理大规模数据

'''

odd_numbers = list(filter(lambda x: x % 2 == 1, [1, 2, 3]))  # 输出：[1, 3]