def myreduce(anyfunc, sequence):
    result = sequence[0]
    for item in sequence[1:]:
        result = anyfunc(result, item)
    return result
l=[1,2,3,4,5]
x=[]
x.append(myreduce(lambda x,y: x+y , l))
print(x)
''' Output 
[15]
'''

