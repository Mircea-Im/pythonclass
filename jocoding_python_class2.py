# # class
# result = 0
# def add(num):
#     global result
#     result += num
#     return result
# print(add(3))
# print(add(4))
# result = 1
# print(add(3))

# # 클래스를 이용한 계산기
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def add(self,num):
#         self.result += num
#         return self.result
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# print(cal1.add(3))
# print(cal1.add(4))

# class - 과자 틀 , 과자(객체)

# class Fourcal:
#     pass
# a = Fourcal()
# print(a)

# class Fourcal:
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second
# a = Fourcal()
# a.setdata(1,2)
# print(a.first)
# print(a.second)

# class Fourcal:
#     def __init__(self,first,second):
#         self.first = first
#         self.second = second
#
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
# # a = Fourcal()
# # a.setdata(4,2)
# # print(a.add())
#
# # 클래스의 상속
# class MoreFourcal(Fourcal):
#     pass
# a = MoreFourcal(4,2)
# print(a.add())

# 구구단 만들기
# def GuGu(n):
#     result = []
#     for i in range(1,10):
#         result.append(n*i)
#     return result
#
# print(GuGu(2))

# sum = 0
# for i in range(1,1000):
#     if i%3 ==0 or i%5 == 0 :
#         sum += i
# print(sum)

# def GetTotalPage(m,n):
#     if m%n == 0:
#         return m//n
#     else:
#         return m//n + 1
#
# print(GetTotalPage(5,10))

# 모든 python파일 확인하기
# import os
#
# def search(dirname):
#     try :
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname,filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else :
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == ".py":
#                     print(full_filename)
#     except PermissionError:
#         pass
# search("C:/")