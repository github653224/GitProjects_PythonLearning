#装饰器

def make_cake():
    return 'cake'

def add_candles(cake_func):
    def insert_cadles():
        return cake_func+' candles'
    return insert_cadles()


gift_func=add_candles(make_cake())
print(gift_func)