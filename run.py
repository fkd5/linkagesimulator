


if __name__ == "__main__":
	printbackground()
	joint = getjointsfromuser()
	printjoints(joint)
	ITERATIONS = 20
	getinitialmomentum(joint)
	for i in range(0, ITERATIONS):
		applymomentum(joint)
		printjoints(joint)
		#wait 2 seconds



def getjointsfromuser():
	'''
	Gets list of joints by user input.

	INPUT: none

	RETURN:
		firstjoint: *joint*
			First joint on linked list of joints.
	'''

	#prevjoint = Null
	#FIRST one not part of while loop
	# get loc and weight
	# set to prevjoint
	#while loop for while user still wants to input joints (input isn't 'stop' or more than 10 joints)
		#get joint location by asking for angle and user some function somewhere
			#prevjoint.findlocfromangle()
		#get joint weight
		# attach to prevjoint
		# printjoints(firstjoint)
	#ask user if they want to attach the first and last joint to make a circle thing


	return firstjoint


def getjointsfromfile():
	'''
	Gets list of joints from file input
	'''
	pass


def printbackground():
	'''
	Print background. Have cool looking blue or red background with time counter in corner and maybe a
	frame thing or a pattern in the background.
	'''

	pass


def printjoints(joint):
	'''
	Print joints to file with links and ID numbers.  Joints in black to white depending on weight.
	Links in between joints.  ID numbers next to joints (or inside the joints in strong color).
	

	basically just use imagedraw module from PIL for everything.
	https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
	'''


def getinitialmomentum(joint):
	'''
	Get momentum from user.  Also ask which joint to apply momentum to.
	Assign momentum to correct joint.
	'''


def applymomentum(joint):
	'''
	DO STUFF
	'''