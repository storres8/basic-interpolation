print("hello {} this is writtin in {}".format('steven', 'python'))
#prints out "hello steven this is writtin in python"

#we can also include the index values that we want to be interpolated
print("hello {1}, this is writtin in {0}".format('python', 'steven'))
# when we do it this way we don't have to put the words we want interpolated
# we in order. Rather, we can insert them through knowing their index value

# we can also assign the words we want interpolated as values to a variable
# and this way we don't have to know their index, but rather their variable
print('helloooo {s} this is writtin in {p}'.format(p='python', s='steven'))
#all these methods are valid if we use the .format() function for interpolation
#also since the variables are pointing to a value we can use that variable
# as many times as we want
print('hello {s} this is writtin in {s}'.format(p='python', s='steven'))
#this might not make sense but it shows that the variables are recyclable


# for numbers there is also float formatting that allows us to change
# how many decimal places we want to round by and the white space before
# the number.

# Float formatting interpolation: "{value:width.precisionf}"
result=100/567
print("The result is {r}".format(r=result))
# prints The result is 0.1763668430335097

print("and this is the result rounded to 3 decimal places {r:1.3f}".format(r=result))
# prints and this is the result rounded to 3 decimal places 0.176

# the width value simply increases the space between the number and the word right
# before it

# We also have f-string literals that is much newer than the .format() method
name="steven"
p="python"
print(f'hello {name} this is writtin in {p} using f-string litrals')
