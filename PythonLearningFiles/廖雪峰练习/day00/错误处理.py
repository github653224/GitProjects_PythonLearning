# try:
#     print("try is starting")
#     r=10/0
#     print("result is ",r)
# except  ZeroDivisionError as e:
#     print("exception is ",e)
# finally:
#     print("Hapended exception")
#
try:
    print("try is starting")
    r=10/0
    print("result is ",r)
except  Exception as e:
    print("exception is ",e)
finally:
    print("Hapended exception")