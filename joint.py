
class Joint:
	'''
	A joint.
	'''

	def __init__(self, ID, loc, pred=None, suc=None, weight=1, mdir=(0,0)):
		'''
		init
		'''

		IDnumber = ID
		location = loc
		pred = pred
		suc = suc
		weight = weight
		mdirection = mdir


	def changesuc(self, joint):
		self.suc = joint


	def changepred(self, joint):
		self.pred = joint


	def changeloc(self, movement):
		self.loc = (self.loc[0] + movement[0], self.loc[1] + movement[1])


	def getpred(self):
		return self.pred


	def getsuc(self):
		return self.suc


	def getID(self):
		return self.IDnumber


	def getloc0(self):
		return self.location[0]


	def getloc1(self):
		return self.location[1]


	def getweight(self):
		return self.weight


	def getmomentummag(self):
		return math.sqrt(self.mdirection[0]**2 + self.mdirection[1]**2)


	def getmomentum(self):
		return self.mdirection


	def getmomentumdir(self):
		mag = self.getmomentummag()
		return (self.mdirection[0]/mag, self.mdirection[1]/mag)


	def addmomentum(self, mdir):
		'''
		Add current momentum and new momentum as vectors.
		'''
		self.mdirection[0] = self.mdirection[0] + mdir[0]
		self.mdirection[1] = self.mdirection[1] + mdir[1]

	def findnewlocfromangle():



