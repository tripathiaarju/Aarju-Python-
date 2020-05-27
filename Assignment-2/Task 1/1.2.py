def my_filter(func,sequence):
    res=[]
    for variable in sequence :
        if func(variable):
            res.append(variable)
    return res

def is_even(item):
    if item%2==0 :
        return True
    else :
        return False
seq=[1,2,3,4,5,6,7,8,9,10]
print(my_filter(is_even,seq))
''' Output 
[2, 4, 6, 8, 10]
'''