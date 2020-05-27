subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","Cricket"]
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
    print (sentence)
'''OUTPUT
Americans Play Baseball
Americans Play cricket
Americans watch Baseball
Americans watch cricket
Indians Play Baseball
Indians Play cricket
Indians watch Baseball
Indians watch cricket
'''