from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from joint import Joint
import math
LENGTH = 15
length = 15





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
	firstjoint = Joint(ID=1, loc=(20,20), pred=None, suc=None, weight=1, mdir=(4,6))
	firstjoint.changesuc(Joint(ID=2, loc=(20+LENGTH*math.sin(0.3),20+LENGTH*math.cos(0.3)), pred=firstjoint, suc=None, weight=1, mdir=(0,0)))
	return firstjoint


def printbackground():
	'''
	Print background. Have cool looking blue or red background with time counter in corner and maybe a
	frame thing or a pattern in the background.
	'''

	length = 1000

	img = Image.new('RGB', (length, length), color = 'pink')
	img.save('View_Simulator.png')

	pass


def printjoints(joint):
	'''
	Print joints to file with links and ID numbers.  Joints in black to white depending on weight.
	Links in between joints.  ID numbers next to joints (or inside the joints in strong color).

	basically just use imagedraw module from PIL for everything.
	https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
	'''
	#radius of circle
	radius = 15

	img = Image.open('View_Simulator.png')
 
	d = ImageDraw.Draw(img)
	fontsize = 15
	font = ImageFont.load_default()

	d.text((length * .5,0), "Linkage simulator", font=font, fill=(255, 255, 255))

	#draw current joing
	#center of current joint
	cent_x = joint.getloc0
	cent_y = joint.getloc1

	# if joint.getpred() != None:
	# 	#center of previous joint
	# 	cent_x_p = joint.prev.getloc0
	# 	cent_y_p = joint.prev.getloc1

	#center of next joint
	cent_x_s = joint.suc.getloc0
	cent_y_s = joint.suc.getloc1

	#draw the current joint
	weight_curr = joint.weight
	
	#d.ellipse((cent_x - radius, cent_y - radius, cent_x + radius, cent_y + radius), fill = (int(255*weight_curr), int(255*weight_curr), int(255*weight_curr)), outline = 'black')
	d.ellipse((cent_x - radius, cent_y - radius, cent_x + radius, cent_y + radius), fill = 'black', outline = 'black')

	#draw its number
	d.text((cent_x, cent_y), joint.ID, font=font, fill='blue')
	
	# if joint.getpred() != None:
	# 	#draw the line from the previous joint. 
	# 	d.line([(cent_x, cent_y), (cent_x_p, cent_y_p)], fill='grey', width = 5) 

	#draw the next joint
	weight_suc = joint.suc.weight
	d.ellipse((cent_x_s - radius, cent_y_s - radius, cent_x_s + radius, cent_y_s + radius), fill = (int(255*weight_suc), int(255*weight_suc), int(255*weight_suc)), outline = 'black')
	
	#draw its number
	d.text((cent_x_s, cent_y_s), joint.suc.ID, font=font, fill='blue')

	#draw the line to the next joint
	d.line([(cent_x, cent_y), (cent_x_s, cent_y_s)], fill='grey', width = 5)

	img.save('View_Simulator.png')


def getinitialmomentum(joint):
	'''
	Get momentum from user.  Also ask which joint to apply momentum to.
	Assign momentum to correct joint.
	'''


def applymomentum(joint):
	'''
	DO STUFF
	'''

	# # get momentum of joint and apply to pred and suc
	# pred = joint.getpred()
	# suc = joint.getsuc()
	# mdir = joint.getmomentumdir()
	# mmag = joint.getmomentummag()

	# if pred != Null:
	# 	linkdir = joint.diroflink(pred)
	# 	theta = angle(mdir, linkdir)
	# 	axialmovement = mmag * Sin(theta)
	# 	radialmovement = mmag * Cos(theta)

	# # while pred is not Null or suc is not Null or pred ID# != suc ID# or pred.pred ID# != suc ID#
	# 	while ((joint.getpred() == None and joint.getsuc() == None) == False) and joint.getpred().getID() != joint.getsuc().getID() and joint.getpred().getpred().getID() != joint.getsuc().getID():
	# 	# keep propagating momentum
	# 	joint.getmomentumdir()

	firstID = joint.getID
	suc = joint.getsuc()

	while joint.suc != None and suc.getID != firstID:
		# get angle between joint and suc
		linkdir = (joint.getloc0() - suc.getloc0(), joint.getloc1() - suc.getloc1())
		theta = angle(linkdir, joint.getmomentumdir())

		# move joint in radial direction
		radialdir = joint.getmomentumdir
		movement = (suc.getweight() * joint.getmomentummag * math.cos(theta) * radialdir[0], suc.getweight() * joint.getmomentummag * math.cos(theta) * radialdir[1])
		joint.changeloc(movement)
		suc.addmomentum(movement)

		# move joint in angular direction
		circumference = math.pi() * LENGTH**2
		spin = ((joint.getmomentummag + math.sin(theta))/circumference) * 2
		thetaprime = angle((0,1), linkdir)
		spinmove = (LENGTH * (math.sin(thetaprime + spin) - math.sin(thetaprime)). LENGTH * (math.cos(thetaprime) - math.cos(thetaprime + spin)))
		if angle(spinmove, joint.getmomentumdir) < math.pi:
			joint.changeloc(spinmove)
		else:
			joint.changeloc((-spinmove[0], spinmove[1]))


def angle(vector1, vector2):
	dotproduct = (vector1[0]*vector2[0], vector1[1]*vector2[1])
	den = magnitude(vector1) * magnitude(vector2)
	return math.acos(dotproduct/den)

def magnitude(vector):
	return math.sqrt(vector[0]**2 + vector[1]**2)

if __name__ == "__main__":
	printbackground()
	joint = getjointsfromfile()
	printjoints(joint)
	ITERATIONS = 20
	#getinitialmomentum(joint)
	for i in range(0, ITERATIONS):
		applymomentum(joint)
		printjoints(joint)
		#wait 2 seconds