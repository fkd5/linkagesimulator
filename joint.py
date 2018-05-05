
import math 

class Joint:
	'''
	A joint.
	'''

	def __init__(self, n, loc, pred=None, suc=None, weight=1, angle=0):
		'''
		Initialized joint object.
		'''

		self.ID = n
		self.location = loc
		self.pred = pred
		self.suc = suc
		self.weight = weight
		self.angle = angle


	def findnextpos(self, interval):
		'''
		Moves next joint to new location based on movement of current joint.

		INPUT:
			interval: *float*
				Angle by which each joint needs to move on every iteration.
		'''
		ang = self.angle
		LENGTH = 100
		a = LENGTH * math.cos(math.radians(ang)) + self.location[0]
		b = LENGTH * -math.sin(math.radians(ang)) + self.location[1]
		local = (a, b)
		self.suc.location = local
		self.suc.angle += interval

