# -*- coding:utf-8 -*-  


# 1
# lower = int(input("最小值："))
# upper = int(input("最大值："))

# for num in range(lower, upper + 1):
#     if num >1:
#         for i in range(2,num):
#             if(num % i) == 0:
#                 break

#         else:
#             print(num)

# # 2
# str = 'stlen'

# print len(str)

# 3.猴子分桃子，第一只分五份，多一个扔了；第二只分五份，多一份扔了；第三只。。。
# if __name__ == '__main__':
#     i = 0
#     j = 1
#     x = 0
#     while (i < 5):
#         x = 4*j
#         for i in range(0,5):
#             if(x%4 != 0):
#                 break
#             else:
#                 i += 1
#             x = (x/4)*5 +1
#         j += 1
#     print x

# 4、列表化为字典

# i = ['a','b']
# l = [1,2]
# print dict([i,l])

# 5、合并文件a,b到c

# if __name__ == '__main__':
#     import string
#     fp = open('G:\\test1.txt')
#     a = fp.read()
#     fp.close()

#     fp = open(r'G:\test2.txt')
#     b = fp.read()
#     fp.close()

#     fp = open("G:\\test3.txt",'w')
#     l = list(a + b)
#     # l.sort()
#     s = ''
#     s = s.join(l)
#     fp.write(s)
#     fp.close()


# 6.转化字母

# if __name__ == '__main__':
#     fp = open('G:\\test.txt','w')
#     string = raw_input('please input a string: \n')
#     string = string.upper()
#     fp.write(string)
#     fp = open('G:\\test.txt','r')
#     print fp.read()
#     fp.close()

# 7.读取7个数，读取一个值，打印出数值个数的*

# if __name__ == '__main__':
#     n = 1
#     while n<=7:
#         a = int(raw_input('input a number:\n'))
#         while a < 1 or a > 50:
#             a = int(raw_input('input a number:\n'))

#         print a * '*'
#         n +=1
# 8、0-7能组成奇数的个数,个位数为4，二个数为7*4，三个数为7*8*4，四个数为7*8*8*4

if __name__ == '__main__':
    sum = 4
    s = 4 
    for j in range(2,9):
        print sum
        if j<=2:
            s*=7
        else:
            s*=8
        sum+=s

    print 'sum=%d' % sum 



