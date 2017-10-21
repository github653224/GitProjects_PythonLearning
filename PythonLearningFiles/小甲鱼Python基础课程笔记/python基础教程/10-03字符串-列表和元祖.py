str1='I love fishc.com'
print(str1[:6]) #对列表进行切片
print(str1[5])

str1=str1[:6]+'插入的字符串'+str1[6:]
print(str1)

#字符串的格式化
s1='{0} love {1}.{2}'
print(s1)
s2=s1.format('I','fishc','com')
print(s2)

print('%c %c %c' % (97,65,48))

print('%s'% 'I love fishc.com')

print('%d + %d =%d' % (4,5,9))