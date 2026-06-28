test_dict={'Codingal':3,'is':5,'best':0,'for':5,'coding':5}
print("the original dictionary:"+str(test_dict))
k=2
res=0
for key in test_dict:
    if test_dict[key]==5:
        res=res+1
print("frequency of 5 is",str(res))