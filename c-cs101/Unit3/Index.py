# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.
def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1
# <list>.index(<value>) operate
#    return list_n.index(at)

# <value> in <list> operate   will return True or False
#    return at in list_n

# <value> not in <list> <==> not <value> in <list>

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
