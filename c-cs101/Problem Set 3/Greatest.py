# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(p):
    big = 0
    for i in p:
	if i > big:
	    big = i
    return big
#    num = 0
#    i = 0
#    for e in p:        
#        if i == 0:            
#            num = e
#        else:            
#            if num >= e:                
#                num = num
#            else:                
#                num = e  
#        i = i + 1
#    return num
    
print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
