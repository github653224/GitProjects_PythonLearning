def discounts(price,rate):
    final_price=price*rate
    old_price=50         #这里看似是修改的是全局变量，事实上不是，这时Python会自动在函数体内创建一个
                        #和全局变量一样的名字的局部变量old_price
    print('修改后的old_price是1：',old_price)
    return final_price

#在这里的price 、rate 和 final_price都是局部变量，出了函数都是无效的，是无法在函数外
#访问局部变量的

old_price=float(input('请输入原价:'))
rate=float(input('请输入折扣率:'))

new_price=discounts(old_price,rate)
print('打折后的价格是：',new_price)

print('修改后的old_price是2：', old_price) #在函数体内没有全局变量进行修改成功

#全局变量在函数体内和外都可以访问，但是再函数体内是无法改变的
#局部变量只能在函数体内访问，出了函数就不能访问
#如果想在函数体内对全局变量进行修改就要在函数体内在全局变量前面加上：global