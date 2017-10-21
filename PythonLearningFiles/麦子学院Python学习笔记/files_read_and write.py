some_sentenses="""
I love python
not because it easy
it have a lot of moduls
in it.
"""

f=open('1.txt','w')
f.write(some_sentenses)
f.close()

f=open('1.txt','r')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line)

f.close()