

class fileProperties:
	def __init__(self,n="",s=0,m="b"):
		self.n=n
		self.s=s
		self.m=m
	
	def show(self):
		print(self.n)
		print(self.s)
		print(self.m)

		
def scanFiles(path):
	print("scanning: "+path)
	fp = fileProperties("name",1200,"a")
	fp.show()
	return 0
