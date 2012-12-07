# 
# demo
# try some python stuff
#
import FileSystem.scanner

def square(x):
	try:
		return x*x
	except ValueError as valueerr:
		print(valueerr)
	except Exception as otherErr:
		print(otherErr)


print "hello world"
print "-----------"


x = 4

while x < 10:
	print "the square of "+ str(x)+" is"
	print square(x)
	x+=1

print FileSystem.scanner.scanFiles("/tmp")


