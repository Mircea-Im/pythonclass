# # def sum(a,b):
# #     result = a + b
# #     return result
# # print(sum(1,2))
# #
# # def say():
# #     return 'Hi'
# #
# # print(say())
# #
# # mylist = [1,2,3]
# # mylist.pop()
# # print(mylist)
#
# # def sum_many(*nums):
# #     sum = 0
# #     for i in nums:
# #         sum += i
# #     return sum
# # print(sum_many(1,2,3))
#
# # def sum_many(**kwargs):
# #     for k in kwargs.keys():
# #         if(k == "name"):
# #             print("당신의 이름은 : "+k)
#
# # def sum_and_mul(a,b):
# #     return a+b,a*b
# # print(sum_and_mul(3,7))
#
# # def say_myself(name,old,man = True):
# #     print("나의 이름은 %s 입니다."%name)
# #     print("나이는 %d살 입니다."%old)
# #     if man:
# #         print("남자입니다.")
# #     else:
# #         print("여자입니다.")
# # say_myself('임정훈',30,True)
#
# # a = 1
# # def vartest():
# #     global a
# #     a += 1
# # vartest()
# # print(a)
#
# # add = lambda a,b: a+b
# # print(add(3,4))
#
# # mylist = [lambda a,b: a+b, lambda a,b: a*b]
# # print(mylist[1](1,2))
#
# f = open('새파일.txt','w',encoding="utf-8")
# for i in range(1,11):
#     data = '%d번째 줄입니다.\n'%i
#     f.write(data)
# f.close
#
# f = open("새파일.txt","r",encoding="utf-8")
# while True :
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()
#
# f = open("새파일.txt","r",encoding="utf-8")
# lines = f.readlines()
# for line in lines :
#     print(line,end='') # line.strip("\n)
# f.close()
#
# f = open("새파일.txt","r",encoding="utf-8")
# data = f.read()
# print(data)
# f.close()
#
# # with open("foo.txt","w") as f:
# #     f.write("Life is too short, you need python")
# # f.close()
#
#
#
#
#
#
#
