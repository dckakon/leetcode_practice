nums = [7,2,3,5]
dictionary={}
count=0 
for index, value in enumerate(nums):  
    target= value
    if target in dictionary: 
        count+=1                  #! Hash map
        print (True)
    dictionary[value]=index  
if count==0:
    print(False)
print(dictionary)

    
