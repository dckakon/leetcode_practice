
nums=[-3,4,3,90]
target =0
dictionary ={}
for index,value in enumerate(nums):
    remain=target - value
    if remain in dictionary:
        print([dictionary[remain],index]) 
    dictionary[value]=index