
class Joint:
	'''
	A joint.
	'''

	def __init__(self, ID, loc, pred=Null, suc=Null, weight=1, mloc=0, mdir=0):
		'''
		init
		'''

		LENGTH = 10

		IDnumber = ID
		location = loc
		pred = pred
		suc = suc
		weight = weight
		mlocation = mloc
		mdirection = mdir


	def changesuc(self, joint):
		self.suc = joint


	def changepred(self, joint):
		self.pred = joint


	def addmomentum(self, mloc, mdir):
		'''
		Add current momentum and new momentum as vectors.
		'''

	def findnewlocfromangle()



