# 
# demo
# try some python stuff
#
from FileSystem import scanner as scanner
from FileSystem import fileProperties as prop

def square(x):
	try:
		return x*x
	except ValueError as valueerr:
		print(valueerr)
		return_ok
	except Exception as otherErr:
		print(otherErr)


print "hello world"
print "-----------"


x = 4

while x < 10:
	print "the square of "+ str(x)+" is"
	print square(x)
	x+=1

scanner.scanFiles("/tmp")

prop.readFileProperties("/tmp/movie.avi")
