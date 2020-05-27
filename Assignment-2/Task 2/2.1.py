a = ["This" , "is", "my" , "Check"]
def wordlength(a):
    return list(map(lambda x: len(x),a))
print("Word in length in array =>"+ str(wordlength(a)))
'''OUTPUT
Word in length in array =>[4, 2, 2, 5]
'''