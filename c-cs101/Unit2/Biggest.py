# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

#def bigger(a,b):
#    if a > b:
#	return a
#    return b

def biggest(a,b,c):
    if a > b:
	if a > c:
	    return a
	return c
    if b > c:
        return b
    return c
# use builtin function
#    return max(a,b,c)
# use define bigger function
#    return bigger(bigger(a,b),c)
print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9
