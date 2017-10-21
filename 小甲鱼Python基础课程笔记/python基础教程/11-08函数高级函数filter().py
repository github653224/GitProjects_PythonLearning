# print(help(filter))
temp=range(10)
print(list(temp))


print(list(filter(lambda x:x%2,range(10))))#会过滤是True的元素

print(list(map(lambda x:x*2,range(10))))