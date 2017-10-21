def _private_1(name):
    return "hello , %s" % name

def _private_2(name):
    return "hi , %s " % name

def geeting(name):
    if len(name)>3:
        return _private_1()
    else:
        return _private_2()
