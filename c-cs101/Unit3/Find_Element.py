# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
def find_element(list_n,at):
#    i = 0
#    for e in list_n:
#        if e == at:
#            return i
#        i = i + 1
#    return -1
#    i = 0
#    while i != len(list_n):
#	if list_n[i] == at:
#	    return i
#	i = i + 1
#    return -1

       

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
