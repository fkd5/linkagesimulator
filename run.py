


if __name__ == "__main__":
	joints = getjointsfromuser()
	printbackground()
	printjoints(joints)
	ITERATIONS = 20
	getinitialmomentum(joints)
	for i in range(0, ITERATIONS):
		applymomentum(joints)
		printjoints(joints)
		#wait 2 seconds



def getjointsfromuser():
	'''
	Gets list of joints by user input
	'''


def printbackground():
	'''
	Print background
	'''


def printjoints(joints):
	'''
	Print joints to file with links and ID numbers
	'''


def getinitialmomentum(joints):
	'''
	Get momentum from user.
	Assign momentum to correct joint.
	'''


def assignmomentum(joints):
	'''
	DO STUFF
	'''