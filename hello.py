print "hello world"
print "-----------"

def square(x):
	return x*x

x = 4

while x < 10:
	print "the square of "+ str(x)+" is"
	print square(x)
	x+=1
	
