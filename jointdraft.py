
import math 

class Jointdraft:
	'''
	A joint.
	'''

	def __init__(self, n, loc, pred=None, suc=None, weight=1, angle=0):
		'''
		init
		'''

		self.ID = n
		self.location = loc
		self.pred = pred
		self.suc = suc
		self.weight = weight
		self.angle = angle

	def changesuc(self, joint):
		self.suc = joint


	def changepred(self, joint):
		self.pred = joint


	def addmomentum(self, mloc, mdir):
		'''
		Add current momentum and new momentum as vectors.
		'''

	#def findnewlocfromangle()


	def findnextpos(self):
		ang = self.angle
		LENGTH = 100
		a = LENGTH * math.cos(math.radians(ang)) + self.location[0]
		b = LENGTH * -math.sin(math.radians(ang)) + self.location[1]
		local = (a, b)
		self.suc.location = local

