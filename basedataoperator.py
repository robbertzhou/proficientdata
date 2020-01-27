# -*- coding:utf-8 -*-

#练习基本数据类型操作
#1、dict数据操作
print("=============字典操作==============")
x = {"a" : 1 , "b" : 2 , "c" : 3}
print(x)
print(x["a"])
del x["c"]
for i in x:
    print(i,",",x[i])

#2 列表操作
print("============列表操作============")
y = ["A" , "B" , "C" , "a" , "b" , "c"]
print(y)
#2.1读取列表元素
print("read element is :" + y[0])
print(y[0:3])
#2.2 修改元素值
y[0] = "4"
#2.3 在列表最后插入新元素
y.append(6)
print(y)

