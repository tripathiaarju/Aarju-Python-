x=[]
num= int(input("Enter number of words to be compared : "))
for i in  range(num):
    n= input("Enter Words to compare : ")
    x.append(n)
print(x)
longest =0
word=" "
for i in range(len(x)):
    if len(x[i])>longest :
        word=x[i]
        longest=len(x[i])
print(word,"Length is ",len(word))
'''OUTPUT
Enter number of words to be compared : 5
Enter Words to compare : Aarju
Enter Words to compare : Tripathi
Enter Words to compare : is
Enter Words to compare : learning
Enter Words to compare : Python
['Aarju', 'Tripathi', 'is', 'learning', 'Python']
Tripathi Length is  8
'''