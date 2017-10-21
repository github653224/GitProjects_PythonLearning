#工厂函数，例如：dict()会创建一个字典的实例

dict1={}
dict2=dict1.fromkeys((1,2,3))
print(dict2) #{1: None, 2: None, 3: None}

dict2=dict1.fromkeys((1,2,3),'Number')
print(dict2)#{1: 'Number', 2: 'Number', 3: 'Number'}

dict2=dict1.fromkeys((1,2,3),('one','two','three'))
print(dict2)#{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}

#访问字典的方法：keys(),values(),items()
dict3={}
dict3=dict3.fromkeys(range(32),'赞')
print(dict3)

for eachKye in dict3.keys():
    print(eachKye)

print('1---------------------------1')

for eachValue in dict3.values():
    print(eachValue)

print('2---------------------------2')

for eachItem in dict3.items():
    print(eachItem)