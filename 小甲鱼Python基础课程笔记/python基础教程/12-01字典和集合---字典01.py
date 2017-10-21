#字典是以键值对的形式存储在大括号中
'''
brand=['李宁','耐克','阿迪达斯','鱼C工作室']
slogan=['一切皆有可能','Just do it','Impossible in nothing','让编程改变世界']
print('鱼C工作室的口号是：',slogan[brand.index('鱼C工作室')])
'''

dict1={'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible in nothing','鱼C工作室':'让编程改变世界'}
print('鱼C工作室的口号是：',dict1['鱼C工作室'])

dict2={1:'one',2:'two',3:'three'}
print(dict2[1])
print(dict2[2])
print(dict2[3])


print('====创建字典=====')
dict3=dict((('f',70),('i',105),('s',115),('h',104),('c',67))) #dict()里面传一个参数，所以里面又有一个括号
print(dict3)

dict4=dict(小甲鱼='让编程改变世界',苍进空='让AV征服所有宅男')
print(dict4)

dict4['苍进空']='所有AV从业者都要通过学习编程来提高职业技能' #改变键对应的值
print(dict4)

dict4['爱迪生']='天才就是99%的汗水+1%的灵感，但这1%的灵感远远比99%的汗水更重要'
print(dict4) #如果键不存在，不会报错，会在当前字典中自动创建
