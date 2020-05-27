def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Dividing by zero is not possible ")
except:
    print("Any other exception")

'''OUTPUT
Dividing by zero is not possible 
'''