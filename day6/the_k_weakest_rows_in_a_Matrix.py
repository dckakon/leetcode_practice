l = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]] 
k = 3

dictionary={}
for i in range(len(l)):
    x=0
    for j in range(len(l[i])): 
        x+=l[i][j]
    dictionary[i]=x

dictionary=sorted(dictionary.items(),key=lambda x:x[1])
c_dict=dict(dictionary)   
mylist=list(c_dict.keys())    
print(mylist[:k])

   
            