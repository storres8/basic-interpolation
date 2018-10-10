print("hello {} this is writtin in {}".format('steven', 'python'))
#prints out "hello steven this is writtin in python"

#we can also include the index values that we want to be interpolated
print("hello {1}, this is writtin in {0}".format('python', 'steven'))
# when we do it this way we don't have to put the words we want interpolated
# we in order. Rather, we can insert them through knowing their index value

# we can also assign the words we want interpolated as values to a variable
# and this way we don't have to know their index, but rather their variable
print('helloooo {s} this is writtin in {p}'.format( p='python', s='steven'))
#all these methods are valid if we use the .format() function for interpolation
